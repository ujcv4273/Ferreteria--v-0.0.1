# Generated by Django 2.2.6 on 2020-03-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombreMarca', models.CharField(max_length=10)),
            ],
        ),
    ]