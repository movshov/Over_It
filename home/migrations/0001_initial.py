# Generated by Django 3.1.2 on 2020-10-08 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoneItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_completed', models.DateField(default=datetime.date.today)),
                ('author', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('author', models.TextField(blank=True)),
            ],
        ),
    ]
