from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'achievements'

urlpatterns = [
    path('', views.achievements_list, name='achievements_list'),
    path('add/', views.add_achievement, name='add_achievement'),
    path('edit/<int:pk>/', views.edit_achievement, name='edit_achievement'),
    path('delete/<int:pk>/', views.delete_achievement, name='delete_achievement'),
    path('<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('like/<int:pk>/', views.like_achievement, name='like_achievement'),
    # path('logout/', LogoutView.as_view(template_name='users/login.html'), name='log_out')
]
