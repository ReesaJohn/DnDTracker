from django.db import models
from enum import Enum


class Speeds(models.Model):
    WALKING = 'W'
    FLYING = 'F'
    SWIMMING = 'S'
    CLIMBING = 'C'
    SPEED_CHOICES = (
        (WALKING, 'walking'),
        (FLYING, 'flying'),
        (SWIMMING, 'swimming'),
        (CLIMBING, 'climbing')
    )

    type = models.TextField(choices=SPEED_CHOICES)
    rate = models.PositiveIntegerField()
