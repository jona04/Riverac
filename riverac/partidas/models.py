from django.db import models

# Create your models here.

class EstadioManager(models.Manager):
	def search(self,query):
		return self.get_queryset().filter(
			models.Q(opponent__icontains=query) | models.Q(stadium__icontains=query) | models.Q(championship__icontains=query)
		)
class PartidasManager(models.Manager):
	def search(self,query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query)
		)

class Estadios(models.Model):
	name = models.CharField('Nome',max_length=50)
	city = models.CharField('Cidade',max_length=50)
	state = models.CharField('Estado',max_length=50)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Estadio"
		verbose_name_plural = "Estadios"
		ordering = ['name']

class Campeonatos(models.Model):
	name = models.CharField('Nome',max_length=50)
	year = models.IntegerField('Ano',blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Campeonato"
		verbose_name_plural = "Campeonatos"
		ordering = ['name']

class Times(models.Model):
	first_name = models.CharField('Nome',max_length=50)
	full_name = models.CharField('Nome Completo',max_length=100)
	sigla = models.CharField('Sigla',max_length=10)
	city = models.CharField('Cidade',max_length=50)
	state = models.CharField('Estado',max_length=50)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = "Time"
		verbose_name_plural = "Times"
		ordering = ['first_name']

class Partidas(models.Model):

	STATUS_CHOICE = (
		(0,'Fora de casa'),
		(1, 'Dentro de casa')
	)
	opponent = models.ForeignKey(Times,verbose_name="Oponente",related_name="partida_opponent")
	stadium = models.ForeignKey(Estadios,verbose_name="Estadio",related_name="partida_estadio")
	inside_or_outside = models.IntegerField('Mando de campo',choices = STATUS_CHOICE, blank=False,null=True)
	championship = models.ForeignKey(Campeonatos,verbose_name="Campeonato",related_name="partida_campeonato")
	start_date = models.DateTimeField('Inicio da Partida',null=True,blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)


	#image = S3DirectField(dest='example1',verbose_name='Imagem',null=True,blank=False)

	objects = PartidasManager()

	def __str__(self):
		return "River x %s" % self.opponent

	# @models.permalink
	# def get_absolute_url(self):
	# 	return ('produto',(),{'slug': self.slug})
		
	class Meta:
		verbose_name = "Partida"
		verbose_name_plural = "Partidas"
		ordering = ['start_date']
