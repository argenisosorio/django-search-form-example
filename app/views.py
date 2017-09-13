# -*- coding: utf-8 -*-
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.core.urlresolvers import *
from .models import *


class AppTemplate(TemplateView):
    template_name = "app/index.html"

 
def buscar(request):
    return render(request, 'app/buscar.html')


def busqueda_prueba(request):
    """
    Funcion para probar el metodo get
    """
    if 'q' in request.GET and request.GET['q']:
        mensaje = 'Estas buscando: %r' % request.GET['q']
    else:
        mensaje = 'Haz subido un formulario vacio.'
    return HttpResponse(mensaje)


def busqueda(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        personas = Persona.objects.filter(nombre__icontains=q)
        return render(request, 'app/buscar.html',  {'personas': personas, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')
