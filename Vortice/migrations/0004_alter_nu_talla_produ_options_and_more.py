# Generated by Django 4.0.6 on 2024-09-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0003_alter_nu_talla_cami_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nu_talla_produ',
            options={'verbose_name_plural': '8.2 Numero Tallas Producto '},
        ),
        migrations.AlterModelOptions(
            name='nu_talla_zapa',
            options={'verbose_name_plural': '8.1 Numero Tallas Zapatos '},
        ),
        migrations.AlterModelOptions(
            name='talla_camiseta',
            options={'verbose_name_plural': '8.3 Eleccion de Tallas Camisetas  '},
        ),
        migrations.AlterModelOptions(
            name='talla_zapato',
            options={'verbose_name_plural': '8.4 Eleccion Tallas Zapatos '},
        ),
    ]
