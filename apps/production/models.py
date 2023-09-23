# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'brands'

    def __str__(self):
        return f"{self.brand_name}"
    
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return f"{self.category_name}"

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

    def __str__(self):
        return f"{self.product_name}"

class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey('sales.stores', models.DO_NOTHING)
    product = models.ForeignKey('products', models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    
    
    class Meta:
        db_table = 'stocks'
        #unique_together = (('store', 'product'),)
