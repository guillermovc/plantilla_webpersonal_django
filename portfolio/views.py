from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    # Hacer request con ORM
    projects = Project.objects.all()    # Devuelve todos los objetos del modelo de Proyecto
    # Lo siguiente es inyectar una lista de proyectos al template
    # Usamos un diccionario de contexto como tercer parámetro
    return render(request, "portfolio/portfolio.html", {'projects':projects})