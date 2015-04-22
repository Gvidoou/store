from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Products.models import Product


class ProductList(ListView):
    """
    View for list of products
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['title'] = 'List of products'
        return context


class ProductDetailView(DetailView):
    """
    View for product page
    """
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Product details'
        return context