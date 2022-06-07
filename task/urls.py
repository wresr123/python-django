from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('select/', views.select, name='select'),
    path('signup_cl/', views.signup_cl, name='signup_cl'),
    path('signup_mn/', views.signup_mn, name='signup_mn'),
]
