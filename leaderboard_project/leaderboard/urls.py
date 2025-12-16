from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_leaderboard, name='individual_leaderboard'),
    path('teams/', views.team_leaderboard, name='team_leaderboard'),
]
