# Generated by Django 4.0.6 on 2024-09-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0012_editables_sec_1_imagen_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='editables',
            name='sec_2_imagen_2',
            field=models.FileField(blank=True, help_text='Agencia texto rotativo', null=True, upload_to='girekstudio/'),
        ),
        migrations.AlterField(
            model_name='editables',
            name='sec_2_imagen_1',
            field=models.FileField(blank=True, help_text='Agencia encabezado imagen 1149x800', null=True, upload_to='girekstudio/'),
        ),
    ]
