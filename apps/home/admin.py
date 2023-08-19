# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Brands, Categories, Products, Customers, OrderItems, Orders, Staffs, Stores, Stocks

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
    list_display = ('quantity',)
admin.site.register(Stocks, StocksAdmin)

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'city')
admin.site.register(Customers, CustomersAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_price')
admin.site.register(OrderItems, OrderItemsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date')
admin.site.register(Orders, OrdersAdmin)

class StaffsAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'email')
admin.site.register(Staffs, StaffsAdmin)

class StoresAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'store_name', 'phone', 'city')
admin.site.register(Stores, StoresAdmin)