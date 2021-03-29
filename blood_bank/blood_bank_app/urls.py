# IMPORTS
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    # path('login_user', views.login_user),
    # path('logout_user', views.logout_user),
    # path('profile/<str:id>', views.profile),
]