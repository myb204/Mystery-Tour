from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='treasurehunt-home'),
    path('leaderboard/', views.leaderboard, name='treasurehunt-leaderboard'),
    path('task_one/', views.task_one, name='treasurehunt-task_one'),
    path('task_two/', views.task_two, name='treasurehunt-task-two'),
    path('end/', views.end, name='treasurehunt-end'),
]