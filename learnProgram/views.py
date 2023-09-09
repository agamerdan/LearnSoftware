from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def LearnPython(request):
    return render(request, "app/learnpython.html")

def LearnDjango(request):
    return render(request, "app/LearnDjango.html")

def LearnJava(request):
    return render(request, "app/LearnJava.html")

def temel(request):
    return render(request, "app/temel.html")
