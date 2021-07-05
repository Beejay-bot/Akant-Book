# Generated by Django 3.1.4 on 2021-06-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_transaction_quanties_of_product_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'CASH'), ('POS', 'POS'), ('TRANSFER', 'TRANSFER'), ('CREDIT', 'CREDIT')], default='cash', max_length=50),
            preserve_default=False,
        ),
    ]