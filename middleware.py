from django.shortcuts import redirect 
from random import choice

paises = ['Colombia','Mexico','Canada']



def de_donde_vengo(request):
	return choice(paises)
	#return 'Colombia'

class PaisMiddleware():
	def process_request(self,request):
		pass
		#pais = de_donde_vengo(request)
		#if pais == 'Mexico':
		#	return redirect('http://www.google.com.mx')


