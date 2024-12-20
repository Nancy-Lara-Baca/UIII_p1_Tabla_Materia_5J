# Generated by Django 5.1.3 on 2024-12-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleados',
            old_name='id_empleados',
            new_name='id_empleado',
        ),
        migrations.RenameField(
            model_name='empleados',
            old_name='salarios',
            new_name='salario',
        ),
        migrations.AlterField(
            model_name='empleados',
            name='num_telefono',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='puesto',
            field=models.CharField(max_length=50),
        ),
    ]
