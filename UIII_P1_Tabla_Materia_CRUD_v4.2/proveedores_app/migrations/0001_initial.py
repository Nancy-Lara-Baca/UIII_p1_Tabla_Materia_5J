# Generated by Django 5.1.3 on 2024-12-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id_proveedores', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_producto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=50)),
                ('num_telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
