# Generated by Django 3.1.4 on 2021-07-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210720_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_num',
            field=models.CharField(default='18239e66-e98b-11eb-b39b-b4b52f8277a3', editable=False, max_length=50),
        ),
    ]
