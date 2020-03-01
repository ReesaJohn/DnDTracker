from django.shortcuts import render
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

from .models import Combatant
from .serializers import CombatantSerializer


def get_combatants(request):
    combatants = Combatant.objects.all()
    serializer_data = CombatantSerializer(combatants, many=True).data
    return JsonResponse(
        {
            "combatants": serializer_data
        },
        status=status.HTTP_200_OK,
    )

