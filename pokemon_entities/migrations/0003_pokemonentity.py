# Generated by Django 3.1.13 on 2021-11-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
            ],
        ),
    ]
