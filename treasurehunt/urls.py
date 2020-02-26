from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='treasurehunt-home'),
    path('start/', views.start, name='treasurehunt-start'),
    path('leaderboard/', views.leaderboard.as_view(), name='treasurehunt-leaderboard'),
    path('help/', views.help, name='treasurehunt-help'),
    path('about/', views.about, name='treasurehunt-about'),
    path('faqs/', views.faqs, name='treasurehunt-faqs'),
    path('assistance/', views.assistance, name='treasurehunt-assistance'),
    path('howtoplay/', views.howtoplay, name='treasurehunt-howtoplay'),
    path('qr/', views.qr, name='treasurehunt-qr'),
    path('clue/', views.clue, name='treasurehunt-clue'),
    path('clue/<int:pk>', views.ClueDetailView.as_view(), name='treasurehunt-clue-detail'),
    path('task/', views.task, name='treasurehunt-task'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='treasurehunt-task-detail'),
    path('info/', views.info, name='treasurehunt-info'),
    path('info/<int:pk>', views.InfoDetailView.as_view(), name='treasurehunt-info-detail'),
    path('end/', views.end, name='treasurehunt-end'),
]
