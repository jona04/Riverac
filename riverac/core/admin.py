from django.contrib import admin

from .models import Noticias, Videos
# Register your models here.

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ['title','created_at','uploaded_at']
	search_fields = ['title']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Videos)
admin.site.register(Noticias,NoticiasAdmin)
