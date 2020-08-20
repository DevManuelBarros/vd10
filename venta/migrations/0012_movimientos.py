# Generated by Django 2.2.4 on 2020-08-20 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gral', '0001_initial'),
        ('venta', '0011_auto_20200816_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default='1983-01-17')),
                ('cantidad', models.IntegerField(default=0)),
                ('tipo_documento', models.CharField(default='sys', max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Cliente')),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.OrdenCompra')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Producto')),
            ],
        ),
    ]
