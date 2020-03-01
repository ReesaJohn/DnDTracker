from django.test import TestCase

from .models import AbilityScores, Action, Alignment, Combatant, Language, LegendaryAction, Sense, Skill, Speeds, Trait


# Create your tests here.
class AbilityScoresTester(TestCase):
    def setUp(self):
        AbilityScores.objects.create(
            strength=10,
            dexterity=14,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=16
        )
        AbilityScores.objects.create(
            strength=10,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=16
        )

    def test_get_modifiers(self):
        score_set1 = AbilityScores.objects.get(
            strength=10,
            dexterity=14,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=16
        ).get_modifiers()
        score_set2 = AbilityScores.objects.get(
            strength=10,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=16
        ).get_modifiers()

        self.assertEqual(
            score_set1,
            {
                'str': 0,
                'dex': 2,
                'con': 2,
                'int': -1,
                'wis': 1,
                'cha': 3
            }
        )
        self.assertEqual(
            score_set2,
            {
                'str': 0,
                'dex': 2,
                'con': 1,
                'int': -1,
                'wis': 1,
                'cha': 3
            }
        )


class ActionTester(TestCase):
    def setUp(self) -> None:
        Action.objects.create(
            action_name="Javelin",
            action_description="Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        )
        Action.objects.create(
            action_name="Talon",
            action_description="Melee Weapon Attack: +4 to hit, reach 5 ft. , one target. Hit: 4 (ld4 + 2) slash ing damage."
        )

    def test_action_creation(self):
        javelin = Action.objects.get(action_name="Javelin")
        talon = Action.objects.get(action_name="Talon")
        self.assertIsNotNone(javelin)
        self.assertIsNotNone(talon)


class AlignmentTester(TestCase):
    def setUp(self) -> None:
        Alignment.objects.create(
            morality=0,
            lawfulness=0
        )

    def test_get_alignment(self):
        lawful_good = Alignment.objects.get(morality=0, lawfulness=0)
        self.assertEqual("Lawful Good", lawful_good.get_alignment())


class SkillTester(TestCase):
    def setUp(self) -> None:
        Skill.objects.create(
            skill='AR',
            modifier=4
        )

    def test_creation(self):
        arcana = Skill.objects.get(
            skill='AR'
        )
        self.assertIsNotNone(arcana)


class CombatantTester(TestCase):
    def setUp(self):
        Combatant.objects.create(
            name="Simple"
        )
        Combatant.objects.create(
            name="Normal",
            ac=16,
            max_hp=124
        )

    def test_create_combatant(self):
        simple = Combatant.objects.get(name="Simple")
        normal = Combatant.objects.get(name="Normal")
        self.assertTrue(simple is not None)
        self.assertTrue(normal is not None)

