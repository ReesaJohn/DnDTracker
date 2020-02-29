from django.db import models
from .Action import Action


class LegendaryAction(Action):
    action_cost = models.PositiveIntegerField()
