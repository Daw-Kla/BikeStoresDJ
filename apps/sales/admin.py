from django.contrib import admin
from .models import Customers, OrderItems, Orders, Staffs, Stores
# Register your models here.


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