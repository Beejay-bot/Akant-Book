# Generated by Django 3.1.4 on 2021-06-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210624_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
