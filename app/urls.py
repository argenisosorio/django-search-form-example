# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views
from .views import AppTemplate


urlpatterns = [
    url(r'^$', AppTemplate.as_view(), name='app'),
    url(r'^buscar/$', buscar, name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
    url(r'^contacto$', contacto, name='contacto'),
]