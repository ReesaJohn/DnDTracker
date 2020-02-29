from django.db import models


class AbilityScores(models.Model):
    strength = models.PositiveIntegerField(null=True)
    dexterity = models.PositiveIntegerField(null=True)
    constitution = models.PositiveIntegerField(null=True)
    intelligence = models.PositiveIntegerField(null=True)
    wisdom = models.PositiveIntegerField(null=True)
    charisma = models.PositiveIntegerField(null=True)