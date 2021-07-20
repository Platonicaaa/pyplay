from datetime import timedelta

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from django.shortcuts import get_object_or_404
from django.utils import timezone

from accounts.models import PyPlayyUser
from auctions import models
from auctions.models import Auction


class BidConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_id']
        self.auction_group_id = 'auction_%s' % self.auction_id

        # Join auction group
        async_to_sync(self.channel_layer.group_add)(
            self.auction_group_id,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.auction_group_id,
            self.channel_name
        )

    def receive_json(self, content, **kwargs):
        bid_response = do_bid(self.scope['user'], self.auction_id)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(self.auction_group_id, bid_response)

    def bid_success(self, event):
        # Send message to WebSocket
        self.send_json(event)

    # Receive message from room group
    def bid_failure(self, event):
        # Send message to WebSocket
        self.send_json(event)


def do_bid(user, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if auction.time_ending < timezone.now():
        return {
            'type': 'bid_failure',
            'error_message': 'Auction has expired.'
        }
    elif auction.time_starting > timezone.now():
        return {
            'type': 'bid_failure',
            'error_message': 'Auction has not started.'
        }

    try:
        latest_bid = models.Bid.objects.filter(auction_id=auction).order_by('-bid_time')
        if not latest_bid:
            increase_bid(user, auction)
        else:
            current_winner = PyPlayyUser.objects.filter(id=latest_bid[0].user_id.id)
            if current_winner[0].id != user.id:
                increase_bid(user, auction)
            else:
                return {
                    'type': 'bid_failure',
                    'error_message': 'You already bid for this auction'
                }
    except KeyError as error:
        return {
            'type': 'bid_failure',
            'error_message': error
        }
    return {
        'type': 'bid_success',
        'bids': auction.bids,
    }


def increase_bid(user, auction: models.Auction):
    entity = models.Bid(user_id=user, auction_id=auction, bid_time=timezone.now())
    entity.save()

    auction.bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=5)
    auction.save()
