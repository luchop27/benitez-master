# Generated by Django 4.0.6 on 2024-09-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0030_rename_imagen_rectang_imagenesproyecto_imagen_rectangu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_imagen_2',
        ),
        migrations.AddField(
            model_name='editables',
            name='sec_2_detalle_2',
            field=models.TextField(blank=True, help_text='Agencia a lado de imagen rotando y frase ', max_length=500, null=True),
        ),
    ]
