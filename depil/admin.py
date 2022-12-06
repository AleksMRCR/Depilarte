from django.contrib import admin
from .models import Cliente, Prof, Atencion

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Prof)
admin.site.register(Atencion)
