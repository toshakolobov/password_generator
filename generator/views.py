import getpass
import random

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    specials = list('!@#$%^&*()_+')
    characters = letters
    if request.GET.get('uppercase'):
        characters.extend(list(letter.upper() for letter in letters))
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('specials'):
        characters.extend(specials)
    length = int(request.GET.get('length', 12))
    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': password})

def about(request):
    whoami = getpass.getuser()
    return render(request, 'generator/about.html', {'whoami': whoami})