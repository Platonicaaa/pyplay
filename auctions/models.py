import datetime

from django.contrib import admin
from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import PyPlayyUser

# noinspection DuplicatedCode
class Product(models.Model):
    PRODUCT_GROUPS = (
        ('FRU', 'Fruits'),
        ('VEG', 'Vegetables'),
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=3, choices=PRODUCT_GROUPS)
    pub_date = models.DateTimeField('date_published')

    @admin.display(
        boolean=True,
        description='Published recently?',
    )
    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.description


class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
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
