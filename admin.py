from django.contrib import admin
from herpeto.models import *

class RegistroAdmin(admin.ModelAdmin):
	list_display = ('id','classe','identificacao',)

admin.site.register(Registro, RegistroAdmin)
