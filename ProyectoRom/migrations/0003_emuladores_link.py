# Generated by Django 5.0 on 2023-12-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoRom', '0002_roms_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='emuladores',
            name='link',
            field=models.CharField(default='asd', max_length=100),
        ),
    ]
