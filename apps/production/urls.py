# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.production import views

urlpatterns = [

    # The home page
    #path('', views.index, name='home'),

    path('stocks_table/', views.stocks_table,  name='stocks_table'),
    path('delete_stock/<int:id>/', views.delete_stock, name='delete_stock'),
    path('edit_stock/<int:id>/', views.edit_stock, name='edit_stock'),

    path('products_table/', views.products_table,  name='products_table'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]
