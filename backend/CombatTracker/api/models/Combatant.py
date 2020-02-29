from django.db import models


# Create your models here.
class Combatant(models.Model):
    name = models.CharField(null=False, blank=False)
    ac = models.PositiveIntegerField(null=True)
    max_hp = models.PositiveIntegerField(null=True)
