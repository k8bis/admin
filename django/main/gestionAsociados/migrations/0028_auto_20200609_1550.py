# Generated by Django 3.0.4 on 2020-06-09 20:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0027_auto_20200609_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencialab',
            name='descripcion',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
