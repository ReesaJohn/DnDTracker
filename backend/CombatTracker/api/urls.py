from django.urls import path

from .views import *

urlpatterns = [
    path('api/get_user_creations', get_user_creations),
    path('api/get_monster_names', get_monster_names),
    path('api/get_monster', get_monster),
    # path('api/get_all_monsters', get_monsters)
]