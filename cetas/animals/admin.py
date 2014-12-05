from django.contrib import admin
from fauna.models import *

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('genero','especie','autor','nome',)

class AnimalRegistryAdmin(admin.ModelAdmin):
	list_display = ('animal','destino','id',)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalRegistry, AnimalRegistryAdmin)
