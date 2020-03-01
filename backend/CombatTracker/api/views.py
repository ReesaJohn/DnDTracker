from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import NotFound

import urllib.request
import json

from .models import Combatant
from .serializers import CombatantSerializer


def get_user_creations(request):
    combatants = Combatant.objects.all()
    serializer_data = CombatantSerializer(combatants, many=True).data
    return JsonResponse(
        {
            "combatants": serializer_data
        },
        status=status.HTTP_200_OK,
    )


def get_monster_names(request):
    url = 'http://dnd5eapi.co/api/monsters/'
    serialized_data = urllib.request.urlopen(url=url).read()
    data = json.loads(serialized_data)
    results = data["results"]

    monsters = {"monsters": []}
    for result in results:
        monsters["monsters"].append({
            "index": result["index"],
            "monster_name": result["name"]
        })

    return JsonResponse(monsters, status=status.HTTP_200_OK)


def get_monster(request):
    monster_name = request.GET.get("monster")
    if monster_name is None:
        raise NotFound

    monster_name = monster_name.lower()
    monster_name = monster_name.replace(' ', '-', monster_name.count(' '))
    url = 'http://dnd5eapi.co/api/monsters/' + monster_name
    serialized_data = urllib.request.urlopen(url=url).read()
    data = json.loads(serialized_data)

    ac = data["armor_class"]
    max_hp = data["hit_points"]
    return JsonResponse({
        "name": monster_name,
        "ac": ac,
        "max_hp": max_hp
    }, status=status.HTTP_200_OK)


# def get_monsters(request):
#     monsters_url = 'http://dnd5eapi.co/api/monsters/'
#     serialized_data = urllib.request.urlopen(url=monsters_url).read()
#     data = json.loads(serialized_data)
#     results = data["results"]
#
#     monsters = {"monsters": []}
#     for result in results:
#         index = result["index"]
#         serialized_monster_data = urllib.request.urlopen(url=(monsters_url + index)).read()
#         monster_data = json.loads(serialized_monster_data)
#         monsters["monsters"].append({
#             "name": monster_data["name"],
#             "ac": monster_data["armor_class"],
#             "max_hp": monster_data["hit_points"]
#         })

