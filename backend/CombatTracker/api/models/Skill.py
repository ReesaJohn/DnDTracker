from django.db import models
from enum import Enum


class SkillChoices(Enum):
    AC = "Acrobatics"
    AH = "Animal Handling"
    AR = "Arcana"
    AT = "Athletics"
    DE = "Deception"
    HI = "History"
    INS = "Insight"
    INT = "Intimidation"
    INV = "Investigation"
    ME = "Medicine"
    NA = "Nature"
    PERC = "Perception"
    PERS = "Persuasion"
    RE = "Religion"
    SOH = "Sleight of Hand"
    ST = "Stealth"
    SU = "Survival"


class Skill(models.Model):
    skill = models.CharField(choices=[(tag, tag.value) for tag in SkillChoices])
    modifier = models.IntegerField()