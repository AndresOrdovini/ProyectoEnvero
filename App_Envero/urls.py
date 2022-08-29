from django.urls import path
from App_Envero.views import caracteristicas, equipo, inicio, mercado, problema, solucion, tecnologia

urlpatterns = [
    path('', inicio, name="inicio"),
    path('problema/', problema, name="problema"),
    path('solucion/', solucion, name="solucion"),
    path('caracteristicas/', caracteristicas, name="caracteristicas"),
    path('tecnologia/', tecnologia, name="tecnologia"),
    path('mercado/', mercado, name="mercado"),
    path('equipo/', equipo, name="equipo"),
   
]
