from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_seller
from products import models
from .forms import ProductForm
from .models import ProductGroup


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return is_seller(self.request.user)

    template_name = 'products/index.html'

    def get_queryset(self):
        queryset = models.Product.objects.order_by('-pub_date')

        if 'product_group' in self.request.GET:
            queryset = queryset.filter(product_group_id__name=self.request.GET['product_group'])

        return queryset


class DetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.Product
    template_name = 'products/detail.html'


class CreateView(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class EditView(UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.Product
    form_class = ProductForm
    template_name = 'products/edit.html'
    success_url = reverse_lazy('products:index')
