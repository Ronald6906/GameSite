from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def cart(request):
    return render(request, 'Cart.html', {})

def eldenring(request):
    return render(request, 'Elden Ring.html', {})

def forzahorizon(request):
    return render(request, 'Forza horizon 5.html', {})

def gtav(request):
    return render(request, 'GTA V.html', {})

def re4(request):
    return render(request, 're4.html', {})

def spiderman(request):
    return render(request, 'spiderman2.html', {})

def uncharted(request):
    return render(request, 'Uncharted.html', {})

def warhammer(request):
    return render(request, 'warhammer.html', {})

def witcher(request):
    return render(request, 'Witcher 3.html', {})

def register(request):
    return render(request, 'Register.html', {})