from django.shortcuts import render
from .models import Curso, Interesse, Sobre

def home(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    sobre = Sobre.objects.first()
    return render(request, 'blog/home.html', {
        'cursos': cursos,
        'interesses': interesses,
        'sobre': sobre,
    })

