from django.db import models  # noqa F401

# your models here
class Pokemon (models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='pokemons')

    def __str__(self):
        return f'{self.title}'

class PokemonEntity (models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)