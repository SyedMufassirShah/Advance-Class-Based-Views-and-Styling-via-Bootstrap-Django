# Generated by Django 5.0.2 on 2024-04-29 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reminders',
            new_name='Reminder',
        ),
    ]
