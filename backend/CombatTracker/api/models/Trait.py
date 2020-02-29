from django.db import models


class Trait(models.Model):
    trait_name = models.CharField(max_length=255)
    trait_description = models.CharField()
