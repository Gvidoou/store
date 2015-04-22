from django.contrib import admin
import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Product, ProductAdmin)