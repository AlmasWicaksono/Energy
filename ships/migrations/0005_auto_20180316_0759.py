# Generated by Django 2.0 on 2018-03-16 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0004_jetty_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship',
            old_name='sscl',
            new_name='sscs',
        ),
    ]
