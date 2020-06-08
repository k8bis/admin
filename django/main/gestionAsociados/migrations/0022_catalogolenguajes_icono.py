# Generated by Django 3.0.4 on 2020-06-06 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0021_auto_20200606_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogolenguajes',
            name='icono',
            field=models.FileField(default=0, upload_to='lenguajes/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
            preserve_default=False,
        ),
    ]