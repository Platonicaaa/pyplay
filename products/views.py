from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_buyer
from products import models
from .forms import ProductForm


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return is_buyer(self.request.user)

    template_name = 'products/index.html'

    def get_queryset(self):
        queryset = models.Product.objects.order_by('-pub_date')

        if 'category' in self.request.GET:
            queryset = queryset.filter(category=self.request.GET['category'])

        return queryset


class DetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Product
    template_name = 'products/detail.html'


class CreateView(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class EditView(UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        return is_buyer(self.request.user)

    model = models.Product
    form_class = ProductForm
    template_name = 'products/edit.html'
    success_url = reverse_lazy('products:index')
