# Generated by Django 2.2.4 on 2019-10-21 20:10

from django.db import migrations, models
import django.db.models.deletion
from  django.apps import apps

def cargar_cliente_inicial(apps, schema_editor):
    responsable = 'Responsable Inscripto'
    cliente = apps.get_model('gral', 'Cliente')
    array_cliente =[cliente(razon_social = 'Arca Distribuciones',
                            nombre_corto = 'Tsu',
                            cuit = '30-68630937-8',
                            direccion_fiscal = 'Francia 3553, Villa Lynch, Bs.As.',
                            direccion_entrega = 'Av. San Martin 1439',
                            condicion_iva =  responsable
                            ),
                    cliente(razon_social = 'Lady Way S.R.L',
                            nombre_corto = 'Violeta',
                            cuit = '30-65146422-2',
                            direccion_fiscal = 'Agüero 568,P.1 Depto"C", CABA',
                            direccion_entrega = 'Av. Gral. Urquiza, Caseros, Bs.As',
                            condicion_iva =  responsable
                            ),
                    cliente(razon_social = 'Matiz S.A',
                            nombre_corto = 'Gigot',
                            cuit = '30-62743503-3',
                            direccion_fiscal = 'Virrey Cavallos 1485, CABA',
                            direccion_entrega = 'Constitucion 1667, CABA',
                            condicion_iva =  responsable
                            )
                    ]
    for item_cliente in array_cliente:
        obj = item_cliente
        obj.save()
    
    


class Migration(migrations.Migration):
    

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=150, unique=True)),
                ('nombre_corto', models.CharField(max_length=25, unique=True)),
                ('cuit', models.CharField(max_length=15, unique=True)),
                ('direccion_fiscal', models.CharField(max_length=250)),
                ('direccion_entrega', models.CharField(max_length=250)),
                ('condicion_iva', models.CharField(default='Responsable Inscripto', max_length=100)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaInsumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaPeso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LineaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True)),
                ('familiaproducto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.FamiliaProducto')),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('abreviatura', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValoresEconomicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('observacioens', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Cliente')),
                ('etiqueta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gral.Etiqueta')),
                ('lineaproducto_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gral.LineaProducto')),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('abreviatura', models.CharField(max_length=5, unique=True)),
                ('es_principal', models.BooleanField(default=False)),
                ('relacion_de_medida', models.IntegerField()),
                ('familiapeso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.FamiliaPeso')),
            ],
        ),
        migrations.CreateModel(
            name='LineaInsumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
                ('familiainsumos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.FamiliaInsumos')),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medida1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medida2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medida3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lineainsumos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.LineaInsumos')),
                ('medida_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Medicion')),
                ('peso_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gral.Peso')),
            ],
        ),
        migrations.CreateModel(
            name='Cuerpos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('abreviatura', models.CharField(max_length=5, unique=True)),
                ('cantidad_medidas', models.IntegerField()),
                ('medicion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.Medicion')),
            ],
        ),
        migrations.CreateModel(
            name='CondicionDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('valor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ValoresEconomicos_CondicionPago', to='gral.ValoresEconomicos')),
            ],
        ),
        migrations.RunPython(cargar_cliente_inicial),
    ]
