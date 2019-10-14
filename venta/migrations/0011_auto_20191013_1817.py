# Generated by Django 2.2.4 on 2019-10-13 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0010_cronograma_terminada'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentraslado',
            name='formato_de_impresion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='venta.FormatodeImpresion'),
        ),
        migrations.AddField(
            model_name='remito',
            name='formato_de_impresion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='venta.FormatodeImpresion'),
        ),
    ]