from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso

# Create your views here.
def lista_cursos(request):
    curso = Curso.objects.all()
    return HttpResponse(curso[0].nombre)
