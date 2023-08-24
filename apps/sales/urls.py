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
    #path('jsonresponse/customers', views.customers, name='customers'),
    path('stores_table/', views.stores_table,  name='stores_table'),
    #path('test/', views.test,  name='test'),
    #path('test/', views.form_handle, name='test'), 
    #path('jsonresponse/stores', views.stores, name='stores'),
    path('order_items_table/', views.order_items_table,  name='order_items_table'),
    path('load_page_order_items', views.order_items_table, name='order_items'),
    path('orders_table/', views.orders_table,  name='orders_table'),
    #path('jsonresponse/orders', views.orders, name='orders'),
    path('staffs_table/', views.staffs_table,  name='staffs_table'),
    #path('jsonresponse/staffs', views.staffs, name='staffs'),
]
