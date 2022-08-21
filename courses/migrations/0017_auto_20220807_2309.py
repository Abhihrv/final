# Generated by Django 3.1.4 on 2022-08-07 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudentcourse',
            name='semester',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courses.studentsemester'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='semester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='studentsemester_courses', to='courses.studentsemester'),
        ),
    ]