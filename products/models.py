import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

import product_groups.models


# To be deleted
class ProductGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    product_group_id = models.ForeignKey(product_groups.models.ProductGroup, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date_published')

    @admin.display(
        boolean=True,
        description='Published recently?',
    )
    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return '{0} - {1}'.format(self.description, self.product_group_id)
