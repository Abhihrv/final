# Generated by Django 3.1.4 on 2022-08-07 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudentcourse',
            name='grade',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courses.grade'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='grade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='students_with_grade', to='courses.grade'),
        ),
    ]