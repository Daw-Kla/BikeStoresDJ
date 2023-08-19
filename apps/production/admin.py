# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Brands, Categories, Products, Stocks

# Register your models here.

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand_id', 'brand_name')
admin.site.register(Brands, BrandsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
admin.site.register(Categories, CategoriesAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name')
admin.site.register(Products, ProductsAdmin)

class StocksAdmin(admin.ModelAdmin):
    list_display = ()
admin.site.register(Stocks, StocksAdmin)
