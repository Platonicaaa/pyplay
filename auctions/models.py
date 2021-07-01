import datetime

from django.contrib.auth import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Product(models.Model):
    CATEGORIES = (
        ('FRU', 'Fruits'),
        ('VEG', 'Vegetables'),
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    pub_date = models.DateTimeField('date_published')

    @admin.display(
        boolean=True,
        description='Published recently?',
    )
    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.category


class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bids = models.IntegerField(default=0)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now=True)
