from django.shortcuts import render
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
import random
# Create your views here.
#密碼產生器
@login_required
def generator(request):
    return render(request,'generator.html')


@login_required
def password(request):

    if request.GET.get('number-length'):
        length = eval(request.GET.get('number-length'))
    else:
        length = eval(request.GET.get('length'))

    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters+= list('abcdefghijklmnopqrstuvwxyz'.upper())

    if request.GET.get('number'):
        characters+= list('0123456789')

    if request.GET.get('special'):
        characters+= list('!@#$%^&*()_~')    

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'password.html' , {'password': password})

@login_required
def lottery(request):
    return render(request ,"lottery.html")


@login_required
def bmi(request):
    return render(request ,"bmi.html")


@login_required
def gym(request):
    return render(request ,"gym.html")
    
@login_required
def gym1(request):
    return render(request ,"gym1.html")

@login_required
def index(request):
    return render(request ,"index.html")
