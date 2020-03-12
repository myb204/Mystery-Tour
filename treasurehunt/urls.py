from django.urls import path
from . import views
from blog import views as views2

urlpatterns = [
    path('', views.home, name='treasurehunt-home'),
    path('start/', views.start, name='treasurehunt-start'),
    path('leaderboard/', views.leaderboard_search, name='treasurehunt-leaderboard'),
    path('help/', views.help, name='treasurehunt-help'),
    path('about/', views.about, name='treasurehunt-about'),
    path('faqs/', views.faqs, name='treasurehunt-faqs'),
    path('assistance/', views.assistance, name='treasurehunt-assistance'),
    path('howtoplay/', views.howtoplay, name='treasurehunt-howtoplay'),
    path('blog/', views2.home, name='blog-home'),
    path('qr/', views.qr, name='treasurehunt-qr'),
    path('newroute/', views.newroute, name='treasurehunt-newroute'),
    path('admin/', views.admin, name='treasurehunt-admin'),
    path('clue/<int:pk>/', views.ClueDetailView.as_view(), name='treasurehunt-clue-detail'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='treasurehunt-task-detail'),
    path('info/<int:pk>/', views.InfoDetailView.as_view(), name='treasurehunt-info-detail'),
    path('end/', views.end, name='treasurehunt-end'),
]
