from django.db import models

# Create your models here.

class Meta:
	app_label = 'Tasks'
	
class Videos(models.Model):

	title = models.CharField('Titulo',max_length=50) 
	video_url = models.CharField('Url video',max_length=100)
	video_url_img = models.CharField('Url imagem video', max_length=50)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Video"
		verbose_name_plural = "Videos"
		ordering = ['created_at']

class Noticias(models.Model):

	title = models.CharField('Titulo',max_length=50) 
	content = models.TextField('Conteudo')
	#image = S3DirectField(dest='example1',verbose_name='Imagem',null=True,blank=False)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"
		ordering = ['created_at']