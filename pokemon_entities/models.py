from django.db import models  # noqa F401

# your models here
class Pokemon (models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='pokemons')

    def __str__(self):
        return f'{self.title}'
