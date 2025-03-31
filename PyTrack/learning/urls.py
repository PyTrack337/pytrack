from django.urls import path
from . import views
from django.shortcuts import render
from .views import custom_404, register, user_login, user_logout

urlpatterns = [
    #path('', views.index, name='index'),
    path('main/', views.main_page, name='main'),
    path("sub/", lambda request: render(request, 'learning/sub.html'), name='sub'),
    path('about/', views.about_page, name='about'),
    path('lesson1/', views.lesson1, name='lesson1'),
    path('practice1/', views.practice1, name='practice1'),
    path('practice2/', views.practice2, name='practice2'),
    path('practice3/', views.practice3, name='practice3'),
    path('lesson/<int:lesson_id>/', views.get_lesson, name='get_lesson'),
    path('lesson/<str:lesson_id>/', views.get_lesson, name='get_lesson'),
    path('404/', views.error404, name='404'),
    path('', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

handler404 = custom_404