from django.db import models
from .AbilityScores import AbilityScores
from.Alignment import Alignment
from .Speeds import Speeds
from .Skill import Skill
from .Sense import Sense
from .Language import Language
from .Trait import Trait
from .Action import Action
from .LegendaryAction import LegendaryAction


class Combatant(models.Model):

    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    HUGE = 'H'
    GARGANTUAN = 'G'
    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (HUGE, 'Huge'),
        (GARGANTUAN, 'Gargantuan')
    )

    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False, unique=True)
    alignment = models.OneToOneField(Alignment, null=True, on_delete=models.DO_NOTHING)
    size = models.TextField(choices=SIZE_CHOICES)

    ac = models.PositiveIntegerField(null=True)
    max_hp = models.PositiveIntegerField(null=True)
    speeds = models.ManyToManyField(Speeds)

    ability_scores = models.OneToOneField(AbilityScores, null=True, on_delete=models.DO_NOTHING)
    skills = models.ManyToManyField(Skill)
    senses = models.ManyToManyField(Sense)
    languages = models.ManyToManyField(Language)

    traits = models.ManyToManyField(Trait)
    actions = models.ManyToManyField(Action, related_name="action")
    reactions = models.ManyToManyField(Action, related_name="reaction")
    legendary_actions = models.ManyToManyField(LegendaryAction)
    lair_actions = models.ManyToManyField(Action, related_name="lair_action")
