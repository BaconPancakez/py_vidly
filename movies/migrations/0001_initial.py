# Generated by Django 5.1.2 on 2024-10-23 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('number_in_stock', models.IntegerField()),
                ('daily_rate', models.FloatField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
    ]
