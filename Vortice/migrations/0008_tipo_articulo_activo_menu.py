# Generated by Django 4.0.6 on 2024-09-27 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0007_vortice_about_03_imagen_01'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_articulo',
            name='activo_menu',
            field=models.BooleanField(default=False),
        ),
    ]
