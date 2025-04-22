from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('main/', views.main_view, name='main'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/complete/', views.complete_lesson, name='complete_lesson'),
    path("sub/", views.sub, name='sub'),
    path('about/', views.about_page, name='about'),
    path('support/', views.support, name='support'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('404/', views.error404, name='error404'),
]