# Generated by Django 3.1.4 on 2020-12-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='user',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
    ]
