# Generated by Django 3.0.8 on 2020-07-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=200)),
                ('placeCountry', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=1000)),
            ],
        ),
    ]
