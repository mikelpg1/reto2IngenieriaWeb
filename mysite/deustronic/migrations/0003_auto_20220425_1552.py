# Generated by Django 2.2.12 on 2022-04-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deustronic', '0002_auto_20220413_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='clientw_datosContacto',
            new_name='cliente_datosContacto',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_direccion',
            field=models.CharField(max_length=45),
        ),
    ]
