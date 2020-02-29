from django.db import models


class Action(models.Model):
    action_name = models.CharField(max_length=255)
    action_description = models.CharField()
