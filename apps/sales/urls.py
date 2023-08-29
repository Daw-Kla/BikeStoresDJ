# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.sales import views 


urlpatterns = [

    # The home page
    #path('', views.index, name='home'),
    #re_path(r'^.*\.*', views.pages, name='pages'),

    path('customers_table/', views.customers_table,  name='customers_table'),
    path('stores_table/', views.stores_table,  name='stores_table'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),    #??????
    #path('test/', views.create_store, name='test'),                    #form for adding new store test
    path('order_items_table/', views.order_items_table,  name='order_items_table'),
    path('load_page_order_items', views.order_items_table, name='order_items'),
    path('orders_table/', views.orders_table,  name='orders_table'),
    #path('jsonresponse/orders', views.orders, name='orders'),
    path('staffs_table/', views.staffs_table,  name='staffs_table'),
]
