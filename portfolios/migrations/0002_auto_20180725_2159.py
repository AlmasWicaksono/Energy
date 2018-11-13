# Generated by Django 2.0.3 on 2018-07-25 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180725_2159'),
        ('shipments', '0002_remove_shipment_transaction'),
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_contract',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='sales_contract',
            name='seller',
        ),
        migrations.AddField(
            model_name='sales_contract',
            name='buyers',
            field=models.ManyToManyField(related_name='as_buyer', to='home.Company'),
        ),
        migrations.AddField(
            model_name='sales_contract',
            name='contract_type',
            field=models.CharField(choices=[('SPA', 'Sales Purchase Agreement'), ('MSPA', 'Master Sales Purchase Agreement'), ('CN', 'Confirmation Notice')], default='SPA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sales_contract',
            name='sellers',
            field=models.ManyToManyField(related_name='as_seller', to='home.Company'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipments.Shipment'),
            preserve_default=False,
        ),
    ]