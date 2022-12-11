from django.contrib import admin
from .models import Cliente, Prof, Atencion

class AtencionAdmin (admin.ModelAdmin):
    list_display =[
        'nombre','apellido','rut','id_prof','fecha','hora','diab',
    ]
    search_fields = ['nombre']
    list_filter = ['nombre','apellido','rut','id_prof','fecha','hora','diab',]

class ClienteAdmin (admin.ModelAdmin):
    list_display =[
        'nombre','apellido','rut','diab',
    ]
    search_fields = ['nombre']
    list_filter = ['nombre','apellido','rut','diab',]

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Prof)
admin.site.register(Atencion, AtencionAdmin)
