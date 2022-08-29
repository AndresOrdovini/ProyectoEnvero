from django.shortcuts import render


def inicio(self):
    return render(self,"inicio.html")

def problema(self):
    return render(self,"problema.html")

def solucion(self):
    return render(self,"solucion.html")

def caracteristicas(self):
    return render(self,"caracteristicas.html")

def tecnologia(self):
    return render(self,"tecnologia.html")

def mercado(self):
    return render(self,"mercado.html")

def equipo(self):
    return render(self,"equipo.html")