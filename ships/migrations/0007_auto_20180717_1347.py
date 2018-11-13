# Generated by Django 2.0.3 on 2018-07-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0006_auto_20180318_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship_shore_compatibility',
            old_name='sscl_doc',
            new_name='sscs_doc',
        ),
        migrations.RemoveField(
            model_name='ship_shore_compatibility',
            name='sscl_date_time',
        ),
        migrations.AddField(
            model_name='ship_shore_compatibility',
            name='sscs_date_time',
            field=models.DateField(auto_now=True, help_text='Date of SSCS'),
        ),
        migrations.AlterField(
            model_name='ship',
            name='sscs',
            field=models.ManyToManyField(through='ships.Ship_Shore_Compatibility', to='terminals.Jetty'),
        ),
        migrations.AlterField(
            model_name='ship_shore_compatibility',
            name='jetty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminals.Jetty'),
        ),
        migrations.DeleteModel(
            name='Jetty',
        ),
    ]