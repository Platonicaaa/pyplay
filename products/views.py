from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_seller
from products import models
from .forms import ProductForm


class IndexView(UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return is_seller(self.request.user)

    template_name = 'products/index.html'

    def get_queryset(self):
        queryset = models.Product.objects.prefetch_related('product_group_id').order_by('-pub_date')

        if 'product_group' in self.request.GET:
            queryset = queryset.filter(product_group_id__name=self.request.GET['product_group'])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        product_groups = models.Product.objects.values_list('product_group_id__name', flat=True).distinct()
        # Add in a QuerySet of all the books
        context['product_groups'] = product_groups
        return context


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
