# Generated by Django 3.1.4 on 2022-07-31 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='semester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='studentcourse_semester', to='courses.semester'),
        ),
    ]