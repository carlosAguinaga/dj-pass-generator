from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnrstuvwxyz')

    generate_password = ''
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('=*"·$)%!:;Ç$'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    for x in range(length):
        generate_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generate_password})
