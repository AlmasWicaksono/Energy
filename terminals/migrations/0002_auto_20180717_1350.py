# Generated by Django 2.0.3 on 2018-07-17 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jetty',
            old_name='Terminal',
            new_name='terminal',
        ),
    ]
