# Generated by Django 5.1.2 on 2024-10-23 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 23, 16, 6, 26, 224007, tzinfo=datetime.timezone.utc)),
        ),
    ]
