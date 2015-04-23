from django.contrib import admin

from apps.products import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('name',)}
    view_on_site = True

admin.site.register(models.Product, ProductAdmin)