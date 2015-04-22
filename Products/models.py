from django.db import models


class Product(models.Model):
    """
    main model for product
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    """
    Model for storing comments
    """
    title = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=False)
    product = models.ForeignKey(Product, blank=False)