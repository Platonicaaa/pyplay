from django.contrib import admin

# Register your models here.
from auctions.models import Auction, Watchlist, Bid

admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
