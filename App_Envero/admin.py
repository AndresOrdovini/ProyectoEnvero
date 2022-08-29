from atexit import register
from django.contrib import admin
from .models import caracteristicas, equipo, inicio, mercado, problema, solucion, tecnologia

# Register your models here.

admin.site.register(inicio)
admin.site.register(problema)
admin.site.register(solucion)
admin.site.register(caracteristicas)
admin.site.register(tecnologia)
admin.site.register(mercado)
admin.site.register(equipo)