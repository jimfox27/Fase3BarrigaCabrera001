# Generated by Django 3.1.2 on 2020-11-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0042_auto_20201128_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='user.png', upload_to=''),
        ),
    ]
