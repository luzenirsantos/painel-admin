from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'loja/index.html', {}) 

def base(request):
    return render(request, 'loja/base.html', {}) 

def base_form(request):
    return render(request, 'loja/base_form.html', {}) 

def base_list(request):
    return render(request, 'loja/base_list.html', {}) 

def erro(request):
    return render(request, 'loja/erro.html', {})

def blank(request):
    return render(request, 'loja/blank.html', {})

def charts(request):
    return render(request, 'loja/charts.html', {})

def password(request):
    return render(request, 'loja/password.html', {})    

def login(request):
    return render(request, 'loja/login.html', {})    

def register(request):
    return render(request, 'loja/register.html', {})   

def tables(request):
    return render(request, 'loja/tables.html', {})    

   