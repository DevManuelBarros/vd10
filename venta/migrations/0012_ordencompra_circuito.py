# Generated by Django 2.2.4 on 2019-10-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0011_auto_20191013_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='circuito',
            field=models.CharField(choices=[('Facturar', 'Facturar'), ('Consignacion', 'Consignacion')], default='Facturar', max_length=12),
        ),
    ]