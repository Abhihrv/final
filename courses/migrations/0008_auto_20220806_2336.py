# Generated by Django 3.1.4 on 2022-08-06 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20220806_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='friday',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='monday',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='thursday',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='tuesday',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='wednesday',
            field=models.BooleanField(default=0),
        ),
    ]
