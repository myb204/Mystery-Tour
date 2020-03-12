from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('treasurehunt.urls')),
    path('blog/', include('blog.urls')),
    path('blog/register/', user_views.register, name='register'),
    path('blog/profile/', user_views.profile, name='profile'),
    path('blog/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('blog/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('blog/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('blog/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('blog/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)