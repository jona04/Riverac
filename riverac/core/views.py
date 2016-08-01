from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	# categorias = Categorias.objects.all()
	# campanha = BannerPrincipal.objects.all()
	context = {}
	# context['campanha'] = campanha[0]
	# context['categorias'] = categorias
	# context['titulo_pagina'] = 'THE Brindes'
	
	return render(request,'index.html',context)