# Generated by Django 3.2.13 on 2023-08-27 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stocks',
            unique_together=set(),
        ),
    ]
