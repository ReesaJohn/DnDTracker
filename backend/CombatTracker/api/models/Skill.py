from django.db import models
from enum import Enum


class Skill(models.Model):
    ACROBATICS = 'AC'
    ANIMAL_HANDLING = 'AH'
    ARCANA = 'AC'
    ATHLETICS = 'AT'
    DECEPTION = 'DE'
    HISTORY = 'HI'
    INSIGHT = 'INS'
    INTIMIDATION = 'INT'
    INVESTIGATION = 'INV'
    MEDICINE = 'ME'
    NATURE = 'NA'
    PERCEPTION = 'PERC'
    PERSUASION = 'PERS'
    RELIGION = 'RE'
    SLEIGHT_OF_HAND = 'SOH'
    STEALTH = 'ST'
    SURVIVAL = 'SU'
    SKILL_CHOICES = (
        (ACROBATICS, "Acrobatics"),
        (ANIMAL_HANDLING, "Animal Handling"),
        (ARCANA, "Arcana"),
        (ATHLETICS, "Athletics"),
        (DECEPTION, "Deception"),
        (HISTORY, "History"),
        (INSIGHT, "Insight"),
        (INTIMIDATION, "Intimidation"),
        (INVESTIGATION, "Investigation"),
        (MEDICINE, "Medicine"),
        (NATURE, "Nature"),
        (PERCEPTION, "Perception"),
        (PERSUASION, "Persuasion"),
        (RELIGION, "Religion"),
        (SLEIGHT_OF_HAND, "Sleight of Hand"),
        (STEALTH, "Stealth"),
        (SURVIVAL, "Survival")
    )

    skill = models.TextField(choices=SKILL_CHOICES)
    modifier = models.IntegerField()
