from django.db import models
# Create your models here.
from django.utils import timezone

import products.models
from accounts.models import PyPlayyUser


class Auction(models.Model):
    product_id = models.ForeignKey(products.models.Product, on_delete=models.CASCADE)
    bids = models.IntegerField(default=0)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    def is_active(self):
        now = timezone.now()
        return (self.time_starting <= now) and (self.time_ending >= now)

    def status(self):
        return 'Active' if self.is_active() else 'Expired'


class Watchlist(models.Model):
    user_id = models.ForeignKey(PyPlayyUser, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)


class Bid(models.Model):
    user_id = models.ForeignKey(PyPlayyUser, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now=True)
