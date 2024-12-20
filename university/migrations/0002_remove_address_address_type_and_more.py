# Generated by Django 5.1.1 on 2024-09-25 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='address',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address_current',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address_home',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='address', to='university.address'),
        ),
        migrations.DeleteModel(
            name='AddressType',
        ),
        migrations.DeleteModel(
            name='Desgination',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
