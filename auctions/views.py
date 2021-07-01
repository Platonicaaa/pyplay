import pdb
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from accounts.models import PyPlayyUser
from auctions import models


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'auctions/index.html'

    def get_queryset(self):
        return models.Auction.objects.order_by('-time_starting')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Auction
    template_name = 'auctions/detail.html'


@login_required
def bid(request, auction_id):
    auction = get_object_or_404(models.Auction, pk=auction_id)
    if auction.time_ending < timezone.now():
        return render(request, 'auctions/detail.html', {
            'auction': auction,
            'error_message': 'Auction has expired.'
        })
    elif auction.time_starting > timezone.now():
        return render(request, 'auctions/detail.html', {
            'auction': auction,
            'error_message': 'Auction has not started.'
        })

    try:
        if request.session['_auth_user_id']:
            user = PyPlayyUser.objects.get(id=request.session['_auth_user_id'])
            latest_bid = models.Bid.objects.filter(auction_id=auction).order_by('-bid_time')
            if not latest_bid:
                increase_bid(user, auction)
            else:
                current_winner = PyPlayyUser.objects.filter(id=latest_bid[0].user_id.id)
                if current_winner[0].id != user.id:
                    increase_bid(user, auction)
                else:
                    return render(request, 'auctions/detail.html', {
                        'auction': auction,
                        'error_message': 'You already bid for this auction'
                    })
    except KeyError as error:
        return render(request, 'auctions/detail.html', {
            'auction': auction,
            'error_message': error
        })
    return HttpResponseRedirect(reverse('auctions:detail', args=(auction_id,)))


def increase_bid(user, auction: models.Auction):
    entity = models.Bid(user_id=user, auction_id=auction, bid_time=timezone.now())
    entity.save()

    auction.bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=5)
    auction.save()
