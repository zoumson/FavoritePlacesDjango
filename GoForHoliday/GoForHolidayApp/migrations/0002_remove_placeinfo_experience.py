# Generated by Django 3.0.8 on 2020-07-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoForHolidayApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeinfo',
            name='experience',
        ),
    ]