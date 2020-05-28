# Generated by Django 2.2.6 on 2020-04-09 21:06

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0109_auto_20200409_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Correo_Cliente',
            field=models.EmailField(blank=True, max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarcorreoexistenteCliente], verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Direccion_Cliente',
            field=models.TextField(max_length=100, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Id_Cliente',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Nombre_Cliente',
            field=models.CharField(help_text='Ingrese el nombre del cliente.)', max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono_Cliente',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='idMarca',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombreMarca',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Descripción'),
        ),
    ]