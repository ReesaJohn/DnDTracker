from django.db import models


def create_alignment(lawfulness='Lawful', morality='Good'):
    morals = {
        "Good": 0,
        "Neutral": 1,
        "Evil": 2
    }
    lawful = {
        "Lawful": 0,
        "Neutral": 1,
        "Chaotic": 2
    }
    return Alignment.objects.create(lawfulness=lawful[lawfulness], morality=morals[morality])


def save_alignment(alignment):
    return alignment.save()


def create_and_save_alignment(lawfulness='Lawful', morality='Good'):
    morals = {
        "Good": 0,
        "Neutral": 1,
        "Evil": 2
    }
    lawful = {
        "Lawful": 0,
        "Neutral": 1,
        "Chaotic": 2
    }
    alignment = Alignment.objects.create(lawfulness=lawful[lawfulness], morality=morals[morality])
    alignment.save()
    return alignment


class Alignment(models.Model):
    LAWFUL = 0
    NEUTRAL = 1
    CHAOTIC = 2
    LAWFULNESS_CHOICES = [
        (LAWFUL, 'Lawful'),
        (NEUTRAL, 'Neutral'),
        (CHAOTIC, 'Chaotic')
    ]

    GOOD = 0
    EVIL = 2
    MORALITY_CHOICES = [
        (GOOD, 'Good'),
        (NEUTRAL, 'Neutral'),
        (EVIL, 'Evil')
    ]

    lawfulness = models.PositiveIntegerField(choices=LAWFULNESS_CHOICES)
    morality = models.PositiveIntegerField(choices=MORALITY_CHOICES)

    def get_alignment(self):
        return self.get_lawfulness() + " " + self.get_morality()

    def get_morality(self):
        return self.MORALITY_CHOICES[self.morality][1]

    def get_lawfulness(self):
        return self.LAWFULNESS_CHOICES[self.lawfulness][1]
