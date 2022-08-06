from django.urls import path
from coder.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", lista_cursos),
    path("estudiante/", estudiante),
    path("profesor/", profesor),
    path("entregables/", entregable)

]