# Generated by Django 2.2.4 on 2019-10-19 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0017_auto_20191018_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configimpresionordentraslado',
            name='type_font_cabecera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCabecera_ordentraslado', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionordentraslado',
            name='type_font_cuerpo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCuerpo_ordentraslado', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionordentraslado',
            name='type_font_pie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuentePie_ordentraslado', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_cabecera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCabecera_remito', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_cuerpo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuenteCuerpo_remito', to='configuraciones.Fuentes'),
        ),
        migrations.AlterField(
            model_name='configimpresionremito',
            name='type_font_pie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuentePie_remito', to='configuraciones.Fuentes'),
        ),
    ]
