from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')
def libros(request):
    return render(request, 'libros/index.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def base(request):
    return render(request, 'base.html')
