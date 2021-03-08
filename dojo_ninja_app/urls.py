from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dojo_submit', views.dojo_submit),
    path('ninja_submit', views.ninja_submit),
]