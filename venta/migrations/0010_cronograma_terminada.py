# Generated by Django 2.2.4 on 2019-10-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0009_auto_20191013_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='terminada',
            field=models.BooleanField(default=False),
        ),
    ]
