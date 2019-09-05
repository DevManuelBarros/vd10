# Generated by Django 2.2.4 on 2019-09-05 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gral', '0002_auto_20190825_0437'),
    ]

    operations = [
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
                ('FamiliaProducto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gral.FamiliaProducto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='LineaProducto_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gral.LineaProducto'),
        ),
    ]
