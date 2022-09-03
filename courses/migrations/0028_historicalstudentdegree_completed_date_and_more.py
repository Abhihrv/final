# Generated by Django 4.1 on 2022-08-23 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_historicalstudentsemester_enrollment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstudentdegree',
            name='completed_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='historicalstudentdegree',
            name='enrollment_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='studentdegree',
            name='completed_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='studentdegree',
            name='enrollment_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
