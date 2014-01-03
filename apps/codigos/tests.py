"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.codigos.models import mdl_codigos
from apps.elementos_comunes.models import mdl_sistema_operativo




class SimpleTest(TestCase):
   def registrar(self):
   		self.sistema = mdl_sistema_operativo.objects.create(nombred='Linux jajja')






