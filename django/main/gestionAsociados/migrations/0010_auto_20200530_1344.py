# Generated by Django 3.0.4 on 2020-05-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0009_auto_20200527_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='ultimamodif',
            field=models.DateField(auto_now=True),
        ),
    ]