# Generated by Django 4.1 on 2022-09-04 21:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('credits', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('credit_required', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('value', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalStudentCourse',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical student course',
                'verbose_name_plural': 'historical student courses',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStudentDegree',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('credits_achieved', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=1, max_digits=2)),
                ('enrollment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('completed_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical student degree',
                'verbose_name_plural': 'historical student degrees',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStudentSemester',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sgpa', models.DecimalField(decimal_places=1, max_digits=2)),
                ('enrollment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical student semester',
                'verbose_name_plural': 'historical student semesters',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTeachingCourse',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical teaching course',
                'verbose_name_plural': 'historical teaching courses',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('monday', models.BooleanField(default=0)),
                ('tuesday', models.BooleanField(default=0)),
                ('wednesday', models.BooleanField(default=0)),
                ('thursday', models.BooleanField(default=0)),
                ('friday', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('from_month', models.IntegerField()),
                ('to_month', models.IntegerField()),
                ('start', models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0))),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits_achieved', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=1, max_digits=2)),
                ('enrollment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('completed_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgpa', models.DecimalField(decimal_places=1, max_digits=2)),
                ('enrollment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='teching_course', to='courses.course')),
            ],
        ),
    ]
