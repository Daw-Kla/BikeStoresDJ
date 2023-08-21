# Generated by Django 3.2.13 on 2023-08-17 15:56

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
    ]