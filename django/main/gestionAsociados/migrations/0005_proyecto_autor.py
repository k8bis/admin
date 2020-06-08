# Generated by Django 3.0.4 on 2020-05-26 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionAsociados', '0004_auto_20200526_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]