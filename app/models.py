# -*- coding: utf-8 -*-
from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=8)

    def __unicode__(self):
        return self.nombre
