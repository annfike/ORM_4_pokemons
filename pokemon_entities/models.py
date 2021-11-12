from django.db import models 


class Pokemon (models.Model):
    title = models.CharField(max_length=200, verbose_name='имя')
    photo = models.ImageField(blank=True, upload_to='pokemons', verbose_name='картинка')
    description = models.TextField(blank=True, verbose_name='описание')
    title_en = models.CharField(max_length=200, blank=True,
                                verbose_name='имя на английском языке')
    title_jp = models.CharField(max_length=200, blank=True,
                                verbose_name='имя на японском языке')
    previous_evolution = models.ForeignKey('self', related_name='next_evolution',
                                          verbose_name='из кого эволюционировал',
                                          on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class PokemonEntity (models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon_entities',         
                            on_delete=models.CASCADE, verbose_name='покемон')
    lat = models.FloatField(default=55, verbose_name='долгота')
    lon = models.FloatField(default=55, verbose_name='широта')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='появился в')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='исчез в')
    level = models.IntegerField(null=True, default=None, blank=True, verbose_name='уровень')
    health = models.IntegerField(null=True, default=None, blank=True, verbose_name='здоровье')
    strength = models.IntegerField(null=True, default=None, blank=True, verbose_name='сила')
    defence = models.IntegerField(null=True, default=None, blank=True, verbose_name='защита')
    stamina = models.IntegerField(null=True, default=None, blank=True, verbose_name='выносливость')