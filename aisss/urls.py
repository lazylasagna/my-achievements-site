from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('achievements/', include('achievements.urls')),
    path('users/', include('users.urls')),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
