from django.shortcuts import render

def LoginView(request):
    return render(request, "login/login.html")

def SiginView(request):
    return render(request, "login/register.html")
