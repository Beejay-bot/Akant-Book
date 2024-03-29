# Generated by Django 3.1.4 on 2021-07-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210720_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_account',
            name='business_email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='Notes',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='income',
            name='Notes',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference_num',
            field=models.CharField(default='cb7106d0-ec01-11eb-8c7f-b4b52f8277a3', editable=False, max_length=50, unique=True),
        ),
    ]
