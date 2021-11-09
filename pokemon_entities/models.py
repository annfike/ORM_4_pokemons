from django.db import models  # noqa F401

# your models here
class PoPokemon (models.Model):
    title = models.CharField(max_length=200)
