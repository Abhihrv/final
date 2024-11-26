# Generated by Django 5.1.1 on 2024-10-11 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_historicalstudentcourse_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudentcourse',
            name='semester',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courses.studentsemester'),
        ),
        migrations.AlterField(
            model_name='historicalstudentcourse',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courses.status'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentsemester_courses', to='courses.studentsemester'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='status_studentcourse', to='courses.status'),
        ),
    ]
