from django.db import models


class AbilityScores(models.Model):
    strength = models.PositiveIntegerField(null=True)
    dexterity = models.PositiveIntegerField(null=True)
    constitution = models.PositiveIntegerField(null=True)
    intelligence = models.PositiveIntegerField(null=True)
    wisdom = models.PositiveIntegerField(null=True)
    charisma = models.PositiveIntegerField(null=True)

    def get_modifiers(self):
        mods = {"str": (self.strength - 10) // 2, "dex": (self.dexterity - 10) // 2,
                "con": (self.constitution - 10) // 2, "int": (self.intelligence - 10) // 2,
                "wis": (self.wisdom - 10) // 2, "cha": (self.charisma - 10) // 2}
        return mods
