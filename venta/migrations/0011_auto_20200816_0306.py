# Generated by Django 2.2.4 on 2020-08-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0010_auto_20200816_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productolineasoc',
            name='fecha_entrega',
            field=models.DateField(default='1983-01-17'),
        ),
    ]