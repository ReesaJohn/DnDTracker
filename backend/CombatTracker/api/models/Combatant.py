from django.db import models
from .AbilityScores import AbilityScores
from .Speeds import Speeds
from .Skill import Skill
from .Sense import Sense
from .Language import Language
from .Trait import Trait
from .Action import Action
from .LegendaryAction import LegendaryAction
from enum import Enum


class Size(Enum):   # A subclass of Enum
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"


class Combatant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, unique=True)
    size = models.CharField(choices=[(tag, tag.value) for tag in Size])
    ac = models.PositiveIntegerField(null=True)
    max_hp = models.PositiveIntegerField(null=True)
    speeds = models.ManyToManyField(Speeds, null=True)

    ability_scores = models.OneToOneField(AbilityScores, null=True)
    skills = models.ManyToManyField(Skill, null=True)
    senses = models.ManyToManyField(Sense, null=True)
    languages = models.ManyToManyField(Language, null=True)

    traits = models.ManyToManyField(Trait, null=True)
    actions = models.ManyToManyField(Action, null=True)
    reactions = models.ManyToManyField(Action, null=True)
    legendary_actions = models.ManyToManyField(LegendaryAction, null=True)
    lair_actions = models.ManyToManyField(Action, null=True)
