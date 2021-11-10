# Generated by Django 3.1.13 on 2021-11-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
