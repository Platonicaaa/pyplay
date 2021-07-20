import pdb
from datetime import timedelta

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from accounts.models import PyPlayyUser
from auctions import models
from auctions.forms import AuctionForm


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return self.request.user.is_buyer()

    template_name = 'auctions/index.html'

    def get_queryset(self):
        return models.Auction.objects.order_by('-time_starting')


class DetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return self.request.user.is_buyer()

    model = models.Auction
    template_name = 'auctions/detail.html'


class CreateView(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return self.request.user.is_buyer()

    model = models.Auction
    form_class = AuctionForm
    template_name = 'auctions/create.html'
    success_url = reverse_lazy('auctions:index')


class EditView(UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        return self.request.user.is_buyer()

    model = models.Auction
    form_class = AuctionForm
    template_name = 'auctions/edit.html'
    success_url = reverse_lazy('auctions:index')

