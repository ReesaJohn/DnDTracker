from django.db import models


class Sense(models.Model):
    sense = models.CharField(max_length=255)