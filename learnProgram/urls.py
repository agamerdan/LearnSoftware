from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('learnPython/', views.LearnPython, name="LearnPython"),
    path('learnDjango/', views.LearnDjango, name="LearnDjango"),
    path('learnJava/', views.LearnJava, name="LearnJava"),
    path('temel/', views.temel, name="temel"),
]
