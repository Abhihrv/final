# Generated by Django 5.1.1 on 2024-10-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_historicalstudentdegree_cgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudentdegree',
            name='completed_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentdegree',
            name='completed_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
