# Generated by Django 3.0.4 on 2020-05-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAsociados', '0011_asociado_apellidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoRedesSociales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fabicon', models.CharField(max_length=20, verbose_name='Logo')),
            ],
        ),
    ]
