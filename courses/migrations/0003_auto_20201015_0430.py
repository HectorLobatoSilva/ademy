# Generated by Django 2.2 on 2020-10-15 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]