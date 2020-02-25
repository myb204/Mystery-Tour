from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='treasurehunt-home'),
    path('start/', views.start, name='treasurehunt-start'),
    path('leaderboard/', views.leaderboard, name='treasurehunt-leaderboard'),
    path('clue/', views.clue, name='treasurehunt-clue'),
    path('task_one/', views.task_one, name='treasurehunt-task_one'),
    path('info/', views.info, name='treasurehunt-info'),
    path('end/', views.end, name='treasurehunt-end'),
]