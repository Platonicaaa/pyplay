import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


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
        return '{0} - {1}'.format(self.description, self.category)
