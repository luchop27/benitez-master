# Generated by Django 4.1.1 on 2022-09-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delifrus', '0012_alter_editable_contac_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='tiktok',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
