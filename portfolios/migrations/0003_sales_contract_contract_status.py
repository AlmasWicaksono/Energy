# Generated by Django 2.0.3 on 2018-07-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_auto_20180725_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_contract',
            name='contract_status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('EFFECTIVE', 'EFFECTIVE')], default='DRAFT', max_length=100),
            preserve_default=False,
        ),
    ]
