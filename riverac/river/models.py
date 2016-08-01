from django.db import models

# Create your models here.

class Jogadores(models.Model):

	POSITION_CHOICE = (
		(0,'Goleiro'),
		(1,'Zagueiro'),
		(2,'Lateral'),
		(3,'Volante'),
		(4,'Meio Campo'),
		(5,'Atacante'),
	)

	first_name = models.CharField('Nome',max_length=50)
	last_name = models.CharField('Sobrenome',max_length=50)
	nickname = models.CharField('Apelido',max_length=10)
	position = models.IntegerField('Posição',choices = POSITION_CHOICE, blank=False,null=True)
	#image = S3DirectField(dest='example1',verbose_name='Imagem',null=True,blank=False)
	Nascimento = models.DateField('Data de Nascimento',blank=True)
	height = models.FloatField('Altura',null=True,blank=True)
	weight = models.DateTimeField('Peso',null=True,blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = "Jogador"
		verbose_name_plural = "Jogadores"
		ordering = ['first_name']

class Patrocinadores(models.Model):

	name = models.CharField('Nome',max_length=50)
	#image = S3DirectField(dest='example1',verbose_name='Logo',null=True,blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Patrocinador"
		verbose_name_plural = "Patrocinadores"
		ordering = ['name']

class Fornecedores(models.Model):

	name = models.CharField('Nome',max_length=50)
	#image = S3DirectField(dest='example1',verbose_name='Logo',null=True,blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Fornecedor"
		verbose_name_plural = "Fornecedores"
		ordering = ['name']

class Parceiros(models.Model):

	name = models.CharField('Nome',max_length=50)
	#image = S3DirectField(dest='example1',verbose_name='Logo',null=True,blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Parceiro"
		verbose_name_plural = "Parceiros"
		ordering = ['name']