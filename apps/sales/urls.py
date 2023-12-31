# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.sales import views 


urlpatterns = [

    # The home page
    #path('', views.index, name='home'),
    #re_path(r'^.*\.*', views.pages, name='pages'),

    path('customers_table/', views.customers_table,  name='customers_table'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'), 
    #path('get_customers_data/', views.get_customers_data, name='get_customers_data'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    path('stores_table/', views.stores_table,  name='stores_table'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'), 
    path('delete_store/<int:store_id>/', views.delete_store, name='delete_store'),
    path('get_stores_data/', views.get_stores_data, name='get_stores_data'),

    #need to be done
    path('order_items_table/', views.order_items_table,  name='order_items_table'),
    path('load_page_order_items', views.order_items_table, name='order_items'),

    path('orders_table/', views.orders_table,  name='orders_table'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'), 
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),

    path('staffs_table/', views.staffs_table,  name='staffs_table'),
    path('edit_staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('get_staffs_data/', views.get_staffs_data, name='get_staffs_data'),

    path('charts_test/', views.charts_test, name='charts_test'),
]
