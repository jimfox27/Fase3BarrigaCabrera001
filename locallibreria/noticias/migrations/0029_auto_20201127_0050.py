# Generated by Django 3.1.2 on 2020-11-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0028_auto_20201101_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(),
        ),
    ]
