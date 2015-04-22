from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Products.models import Product


class ProductList(ListView):
    """
    View for list of products
    """
    model = Product


class ProductDetailView(DetailView):
    """
    View for product page
    """
    model = Product