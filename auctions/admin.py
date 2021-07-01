from django.contrib import admin

# Register your models here.
from auctions.models import Product, Auction, Watchlist, Bid

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
