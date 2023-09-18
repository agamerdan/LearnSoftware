from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView, name="login"),
    path('sigin/', views.SiginView, name="sigin"),
    path('logout/', views.LogOut, name="logout")
]
