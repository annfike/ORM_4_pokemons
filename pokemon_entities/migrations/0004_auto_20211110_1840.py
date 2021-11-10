# Generated by Django 3.1.13 on 2021-11-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20211110_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pokemons', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='имя'),
        ),
    ]
