# Generated by Django 3.1.2 on 2020-11-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0037_auto_20201128_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisis',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
    ]