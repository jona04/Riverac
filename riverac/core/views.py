from django.shortcuts import render
from django.http import HttpResponse


from .models import Noticias

# Create your views here.

def home(request):
	noticia = Noticias.objects.all()
	
	context = {}
	context['noticias'] = noticia
	# context['categorias'] = categorias
	# context['titulo_pagina'] = 'THE Brindes'
	
	return render(request,'index.html',context)

def noticia(request,slug):
	
	noticia = Noticias.objects.get(slug=slug)

	context = {}
	context['noticia'] = noticia

	return render(request,'noticia.html',context)

# Create your views here.

def home(request):
	# categorias = Categorias.objects.all()
	# campanha = BannerPrincipal.objects.all()
	context = {}
	# context['campanha'] = campanha[0]
	# context['categorias'] = categorias
	# context['titulo_pagina'] = 'THE Brindes'
	
	return render(request,'index.html',context)
