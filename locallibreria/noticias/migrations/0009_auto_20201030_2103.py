# Generated by Django 3.1.2 on 2020-10-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0008_auto_20201030_2001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='imagenPost'),
        ),
    ]
