from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_buyer
from auctions import models
from auctions.forms import AuctionForm


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return is_buyer(self.request.user)

    template_name = 'auctions/index.html'

    def get_queryset(self):
        return models.Auction.objects.order_by('-time_starting')


class DetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Auction
    template_name = 'auctions/detail.html'


class CreateView(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Auction
    form_class = AuctionForm
    template_name = 'auctions/create.html'
    success_url = reverse_lazy('auctions:index')


class EditView(UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Auction
    form_class = AuctionForm
    template_name = 'auctions/edit.html'
    success_url = reverse_lazy('auctions:index')
