# Generated by Django 4.0.6 on 2024-09-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0005_rename_s3_imagen_vortice_about_02_imagen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vortice',
            old_name='about_02_imagen',
            new_name='about_04_imagen',
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_subtitulo_04',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_titulo_04',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
