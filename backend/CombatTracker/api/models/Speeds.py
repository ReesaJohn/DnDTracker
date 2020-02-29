from django.db import models
from enum import Enum


class Speeds(Enum):
    W = "walking"
    F = "flying"
    S = "swimming"
    C = "climbing"


class Speeds(models.Model):
    type = models.CharField(choices=[(tag, tag.value) for tag in Speeds])
    rate = models.PositiveIntegerField()