from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante , Profesor , Entregable

# Create your views here.

def inicio(request):
    return render(request, "coder/index.html", {"mensaje": "Vrads es la mejor" })

def estudiante(request):
    return HttpResponse("Vista de estudiante")

def profesor(request):
    return HttpResponse("Vista de profesor")

def entregable(request):
    return HttpResponse("Vista de entregable")

def lista_cursos(request):
    cursos = Curso.objects.all()
    return HttpResponse(cursos[0].nombre)