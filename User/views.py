from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def LoginView(request):
    if request.method == 'POST':
        user=User()
        form=request.POST
        username=form.get('usrnm')
        password=form.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Ulgama Girmani Başardynyz")
            return redirect('index')
        else:
            messages.error(request, "Ulanyjy Ady yada Parolanyz Yalnyşdyr")
            return redirect('login',)
            
    return render(request, "login/login.html")

def SiginView(request):
    if request.method=="POST":
        form=request.POST
        username=form.get('usrnm')
        email=form.get('email')
        password=form.get('password')
        passwordConf=form.get('passwordConf')
        if( password != passwordConf):
            messages.warning(request, 'Parolanyz we gaytadan giren Parolanyz menzeş dal')
            return redirect('sigin')
        user=User.objects.create_user(username=username, password=password)
        if user:
            user.save()
            messages.success(request, 'Başaryly Agza Boldunuz. Ulanjy Ady ve Parolanyzy yazyp ulgama girip bilersiniz')
            return redirect('login')
        
    return render(request, "login/register.html")
