# Generated by Django 3.1.4 on 2021-07-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210718_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_num',
            field=models.CharField(default='8315cfd2-e811-11eb-8012-b4b52f8277a3', editable=False, max_length=50),
        ),
    ]
