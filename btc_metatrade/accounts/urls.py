from django.urls import path
from . import views


urlpatterns = [
    path('signin/',login),
    path('signout/',logout),
    path('signup/',register),
]