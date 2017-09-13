# -*- coding: utf-8 -*-
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.core.urlresolvers import *
from .models import *
from django.core.mail import send_mail
from django.shortcuts import render


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


def contacto(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto', ''):
            errors.append('Por favor introduce el asunto.')
        if not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            print "***** Por favor introduce una direccion de e­mail valida *****"
            errors.append('Por favor introduce una direccion de e­mail valida.')
        if not errors:
            #send_mail( request.POST['asunto'], request.POST['mensaje'],
            #request.POST.get('email', 'noreply@example.com'),
            #['siteowner@example.com'],)
            print "***** mensaje enviado ****"
            return HttpResponseRedirect('/contacto')
    return render(request, 'app/contacto.html', {'errors': errors})
