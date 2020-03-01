from django.urls import path

from .views import get_combatants

urlpatterns = [
    path('api/get_combatants', get_combatants)
]