from django.contrib import admin

from .models import Jogadores,Patrocinadores,Fornecedores,Parceiros

# Register your models here.

admin.site.register(Jogadores)
admin.site.register(Patrocinadores)
admin.site.register(Fornecedores)
admin.site.register(Parceiros)