# Generated by Django 3.0.4 on 2020-06-07 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0023_catalogotiposproyecto_icono'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociado',
            name='foto',
            field=models.FileField(default=0, upload_to='fotosasociados/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
            preserve_default=False,
        ),
    ]
