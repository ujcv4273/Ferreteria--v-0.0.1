# Generated by Django 2.2.6 on 2020-03-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0052_auto_20200317_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='idMarca',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]