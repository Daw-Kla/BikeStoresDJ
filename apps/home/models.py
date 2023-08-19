# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'brands'


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'categories'

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    brand = models.ForeignKey(Brands, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    model_year = models.SmallIntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'products'

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    last_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    phone = models.CharField(max_length=25, db_collation='Polish_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    street = models.CharField(max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)
    state = models.CharField(max_length=25, db_collation='Polish_CI_AS', blank=True, null=True)
    zip_code = models.CharField(max_length=5, db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'

class OrderItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING)
    item_id = models.IntegerField()
    product = models.ForeignKey(Products, models.DO_NOTHING)
    quantity = models.IntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'order_items'
        unique_together = (('order', 'item_id'),)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    order_status = models.SmallIntegerField()
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(blank=True, null=True)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    staff = models.ForeignKey('Staffs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Staffs(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, db_collation='Polish_CI_AS')
    last_name = models.CharField(max_length=50, db_collation='Polish_CI_AS')
    email = models.CharField(unique=True, max_length=255, db_collation='Polish_CI_AS')
    phone = models.CharField(max_length=25, db_collation='Polish_CI_AS', blank=True, null=True)
    active = models.SmallIntegerField()
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffs'


class Stores(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    phone = models.CharField(max_length=25, db_collation='Polish_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)
    street = models.CharField(max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)
    state = models.CharField(max_length=10, db_collation='Polish_CI_AS', blank=True, null=True)
    zip_code = models.CharField(max_length=5, db_collation='Polish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores'

class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Stores, models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'stocks'
        unique_together = (('store', 'product'),)

