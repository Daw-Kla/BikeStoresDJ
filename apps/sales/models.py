from django.db import models
#from apps.production.models import Products
# Create your models here.

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

    def __str__(self):
        return f"(ID: {self.customer_id}) {self.first_name} {self.last_name} "

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

    def __str__(self):
        return self.store_name
    
class OrderItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING)
    item_id = models.IntegerField()
    product = models.ForeignKey('production.Products', models.DO_NOTHING)
    quantity = models.IntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    id = models.AutoField(primary_key=True)

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

    def __str__(self):
        return f"ID: {self.order_id}"
    
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

    #this method allows us to display exatly what we want in admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
