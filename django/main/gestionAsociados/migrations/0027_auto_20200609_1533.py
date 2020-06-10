# Generated by Django 3.0.4 on 2020-06-09 20:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0026_auto_20200607_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='descripcion',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asociado',
            name='intereses',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
