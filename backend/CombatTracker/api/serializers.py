from rest_framework import serializers

from .models.AbilityScores import AbilityScores
from .models.Action import Action
from .models.Alignment import Alignment
from .models.Combatant import Combatant
from .models.Language import Language
from .models.LegendaryAction import LegendaryAction
from .models.Sense import Sense
from .models.Speeds import Speeds
from .models.Skill import Skill
from .models.Trait import Trait


class AbilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityScores
        fields = [
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma'
        ]


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = [
            'action_name',
            'action_description'
        ]


class AlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alignment
        fields = [
            'lawfulness',
            'morality'
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'language_name'
        ]


class LegendaryActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegendaryAction
        fields = [
            'action_name',
            'action_description',
            'action_cost'
        ]


class SenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sense
        fields = [
            'sense',
            'range'
        ]


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = [
            'skill',
            'modifier'
        ]


class SpeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speeds
        fields = [
            'type',
            'rate'
        ]


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = [
            'trait_name',
            'trait_description'
        ]


class CombatantSerializer(serializers.ModelSerializer):
    alignment = AlignmentSerializer(required=False)
    speeds = SpeedsSerializer(required=False, many=True)
    ability_scores = AbilityScoreSerializer(required=False)
    skills = SkillSerializer(required=False, many=True)
    senses = SenseSerializer(required=False, many=True)
    languages = LanguageSerializer(required=False, many=True)
    traits = TraitSerializer(required=False, many=True)
    actions = ActionSerializer(required=False, many=True)
    reactions = ActionSerializer(required=False, many=True)
    legendary_actions = LegendaryActionSerializer(required=True, many=True)
    lair_actions = ActionSerializer(required=False, many=True)

    class Meta:
        model = Combatant
        
        fields = [
            'name',
            'alignment',
            'size',
            'ac',
            'max_hp',
            'speeds',
            'ability_scores',
            'skills',
            'senses',
            'languages',
            'traits',
            'actions',
            'reactions',
            'legendary_actions',
            'lair_actions'
        ]
