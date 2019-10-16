# Generated by Django 2.2.4 on 2019-10-16 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0012_auto_20191015_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_cabecera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCabecera', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_cuerpo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCuerpo', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_pie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuentePie', to='configuraciones.Fuentes'),
        ),
    ]