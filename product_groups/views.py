# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_seller
from product_groups import models
from product_groups.forms import ProductGroupForm


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return is_seller(self.request.user)

    template_name = 'product_groups/index.html'

    def get_queryset(self):
        return models.ProductGroup.objects.all()


class DetailView(UserPassesTestMixin, generic.DetailView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.ProductGroup
    template_name = 'product_groups/detail.html'


class CreateView(UserPassesTestMixin, generic.CreateView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.ProductGroup
    form_class = ProductGroupForm
    template_name = 'product_groups/create.html'
    success_url = reverse_lazy('product_groups:index')


class EditView(UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        return is_seller(self.request.user)

    model = models.ProductGroup
    form_class = ProductGroupForm
    template_name = 'product_groups/edit.html'
    success_url = reverse_lazy('product_groups:index')
