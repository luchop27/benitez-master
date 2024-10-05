# Generated by Django 4.0.6 on 2024-09-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0004_alter_nu_talla_produ_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vortice',
            old_name='s3_imagen',
            new_name='about_02_imagen',
        ),
        migrations.RenameField(
            model_name='vortice',
            old_name='s4_imagen',
            new_name='about_03_imagen',
        ),
        migrations.RenameField(
            model_name='vortice',
            old_name='s5_imagen',
            new_name='about_03_imagen_2',
        ),
        migrations.RemoveField(
            model_name='vortice',
            name='s6_imagen',
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_subtitulo_01',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_subtitulo_02',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_subtitulo_03',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_titulo_01',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_titulo_02',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vortice',
            name='about_titulo_03',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vortice',
            name='s2_imagen',
            field=models.ImageField(blank=True, help_text='sobre nosotros imagen principal imagenes 2000 × 1262 px', null=True, upload_to='vortice'),
        ),
    ]
