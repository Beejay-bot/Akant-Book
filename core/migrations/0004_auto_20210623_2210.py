# Generated by Django 3.1.4 on 2021-06-23 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201216_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.business_account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]