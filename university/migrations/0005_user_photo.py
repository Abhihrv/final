# Generated by Django 5.1.1 on 2024-11-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_remove_teaching_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='assets/university/photos/profile-image-placeholder.jpeg', upload_to='assets/university/photos'),
        ),
    ]
