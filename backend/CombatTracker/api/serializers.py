from .models.Combatant import Combatant
from .models.Action import Action
from .models.Skill import Skill
from .models.Sense import Sense
from .models.LegendaryAction import LegendaryAction

from rest_framework import serializers


class AbilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = [
            'action_name',
            'action_description'
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'skill',
            'modifier'
        ]


class SenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sense
        fields = [
            'sense'
        ]


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = [
            'action_name',
            'action_description'
        ]


class LegendaryActionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = LegendaryAction
        fields = [
            'action_name',
            'action_description',
            'action_cost'
        ]


class CombatantSerializer(serializers.ModelSerializer):
    ability_scores = AbilityScoreSerializer(required=False)
    skills = SkillSerializer(required=False, many=True)
    senses = SenseSerializer(required=False, many=True)
    actions = ActionSerializer(required=False, many=True)
    reactions = ActionSerializer(required=False, many=True)
    legendary_actions = LegendaryActionSerialzer(required=True, many=True)
    lair_actions = ActionSerializer(required=False, many=True)

    class Meta:
        model = Combatant
        
        fields = [
            'name',
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
