# Generated by Django 3.1.4 on 2021-07-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210718_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_num',
            field=models.CharField(default='0cc97868-e988-11eb-8540-b4b52f8277a3', editable=False, max_length=50),
        ),
    ]