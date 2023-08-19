# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
#from apps.sales.models import Stores
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


class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey('sales.Stores', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    
    
    class Meta:
        db_table = 'stocks'
        #unique_together = (('store', 'product'),)
