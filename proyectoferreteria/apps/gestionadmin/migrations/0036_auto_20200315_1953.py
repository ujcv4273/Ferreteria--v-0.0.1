# Generated by Django 2.2.6 on 2020-03-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0035_auto_20200315_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existencia',
            field=models.IntegerField(default=567),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='existenciaMinima',
            field=models.IntegerField(default=789),
            preserve_default=False,
        ),
    ]