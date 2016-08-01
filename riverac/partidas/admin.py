from django.contrib import admin
from .models import Estadios, Times, Campeonatos, Partidas
# Register your models here.

class PartidasAdmin(admin.ModelAdmin):
	list_display = ['opponent','stadium','inside_or_outside','championship','start_date']
	search_fields = ['opponent','stadium','championship']

admin.site.register(Estadios)
admin.site.register(Times)
admin.site.register(Campeonatos)
admin.site.register(Partidas,PartidasAdmin)
