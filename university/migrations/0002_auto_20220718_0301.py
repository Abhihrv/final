# Generated by Django 3.1.4 on 2022-07-18 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_of_type', to='university.addresstype'),
        ),
    ]
