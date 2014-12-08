from django.contrib import admin
from fauna.models import *

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('genero','especie','autor','nome',)

class AnimalRegistryAdmin(admin.ModelAdmin):
	list_display = ('animal','destino','id',)

class AnimalRegistryMonitorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Dados do animal']}),
    ]
    inlines = [AnimalRegistryMonitor]

#class AnimalRegistryMonitorAdmin(admin.ModelAdmin):
#	list_display = ('animal','ponto','metodo',)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalRegistry, AnimalRegistryAdmin)
admin.site.register(AnimalRegistryMonitor, AnimalRegistryMonitorAdmin)
