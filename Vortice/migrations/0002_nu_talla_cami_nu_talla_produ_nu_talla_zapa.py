# Generated by Django 4.0.6 on 2024-09-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nu_Talla_Cami',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_talla_camisetas', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Numero de Tallas Camisetas  ',
            },
        ),
        migrations.CreateModel(
            name='Nu_Talla_Produ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_talla_producto', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '8.4 Tallas Producto ',
            },
        ),
        migrations.CreateModel(
            name='Nu_Talla_Zapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_talla_zapatos', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '8.2 Tallas Zapatos ',
            },
        ),
    ]
