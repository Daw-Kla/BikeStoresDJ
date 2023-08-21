# Generated by Django 3.2.13 on 2023-08-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_collation='Polish_CI_AS', max_length=255)),
                ('last_name', models.CharField(db_collation='Polish_CI_AS', max_length=255)),
                ('phone', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=25, null=True)),
                ('email', models.CharField(db_collation='Polish_CI_AS', max_length=255)),
                ('street', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=50, null=True)),
                ('state', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=25, null=True)),
                ('zip_code', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=5, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'order_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_status', models.SmallIntegerField()),
                ('order_date', models.DateField()),
                ('required_date', models.DateField()),
                ('shipped_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_collation='Polish_CI_AS', max_length=50)),
                ('last_name', models.CharField(db_collation='Polish_CI_AS', max_length=50)),
                ('email', models.CharField(db_collation='Polish_CI_AS', max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=25, null=True)),
                ('active', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'staffs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(db_collation='Polish_CI_AS', max_length=255)),
                ('phone', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=25, null=True)),
                ('email', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=255, null=True)),
                ('street', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=255, null=True)),
                ('state', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=10, null=True)),
                ('zip_code', models.CharField(blank=True, db_collation='Polish_CI_AS', max_length=5, null=True)),
            ],
            options={
                'db_table': 'stores',
                'managed': False,
            },
        ),
    ]
