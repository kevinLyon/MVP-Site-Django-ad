# Generated by Django 2.2 on 2021-01-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_auto_20210115_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, default='anuncios/static/anuncios/img/img.png', null=True, upload_to='anuncios/static/anuncios/img/'),
        ),
    ]
