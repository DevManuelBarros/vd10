# Generated by Django 2.2.4 on 2020-08-10 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField(default='1983-01-17')),
                ('fecha_finalizacion', models.DateField(default='1983-01-17')),
                ('terminada', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='FormatodeImpresion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_externa', models.CharField(max_length=20, unique=True)),
                ('fecha_emision', models.DateField()),
                ('circuito', models.CharField(choices=[('Facturar', 'Facturar'), ('Consignacion', 'Consignacion')], default='Facturar', max_length=12)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Cliente')),
                ('cronograma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Cronograma')),
            ],
        ),
        migrations.CreateModel(
            name='Remito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_externa', models.CharField(max_length=50, unique=True)),
                ('tipo_documento', models.CharField(choices=[('Remito', 'Remito'), ('OrdenTraslado', 'Orden de Traslado')], default='Remito', max_length=50)),
                ('fecha_emision', models.DateField(blank=True, null=True)),
                ('conformado', models.BooleanField(default=False)),
                ('anulado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Cliente')),
                ('formato_de_impresion', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='venta.FormatodeImpresion')),
                ('ordencompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.OrdenCompra')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoLineasRM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cajas', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('total_unidades', models.IntegerField()),
                ('cantidad_confirmada', models.IntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Producto')),
                ('remito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Remito')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoLineasOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('OrdenCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.OrdenCompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Producto')),
            ],
        ),
    ]
