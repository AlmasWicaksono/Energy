# Generated by Django 2.0.3 on 2018-07-17 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0002_auto_20180717_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jetty',
            name='max_ship_draft',
        ),
        migrations.RemoveField(
            model_name='jetty',
            name='max_ship_length',
        ),
        migrations.RemoveField(
            model_name='jetty',
            name='min_ship_length',
        ),
        migrations.RemoveField(
            model_name='jetty',
            name='terminal',
        ),
    ]
