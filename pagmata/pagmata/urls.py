"""
URL configuration for pagmata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('home/', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('turismo/', views.turismo, name="turismo"),
    path('formulario/', views.formulario, name="formulario"),
    path('juego/', views.juego, name="juego"),
    path('destinofinal/', views.destino_final, name="destinofinal"),
    path('pista1/', views.pista1, name="pista1"),
    path('pista2/', views.pista2, name="pista2"),
    path('pista3/', views.pista3, name="pista3"),
    path('pista4/', views.pista4, name="pista4"),
    path('pista5/', views.pista5, name="pista5"),
    path('pista6/', views.pista6, name="pista6"),
    path('descanso/', views.descanso, name="descanso"),

]
