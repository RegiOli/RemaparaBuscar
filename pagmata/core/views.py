from django.shortcuts import render
from .forms import RespuestaFormularioForm, RespuestaDestinoFinalForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Respuesta

def home(request):
    return render(request, "core/home.html")

def index(request):
    return render(request, "core/index.html")

def turismo(request):
    return render(request, "core/turismo.html")



@csrf_exempt
def guardar_respuestas(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Respuesta.objects.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            jugar=data['jugar'],
            caminar=data['caminar'],
            num1=data['num1']
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})



def formulario(request):
    status = None
    if request.method == 'POST':
        form = RespuestaFormularioForm(request.POST)
        if form.is_valid():
            respuesta = form.cleaned_data
            
            lugares_correctos = ["Pacheco", "Parque Centenario", "Planetario", "Abasto", "36 Billares", "CNBA"]
            motivos_correctos = ["Abrazo", "Beso", "Salidas", "Películas", "Juegos", "Nos conocimos"]
            orden_correcto = [5, 6, 3, 4, 2, 1]

            # Verifica las respuestas
            correctas = True
            for i in range(1, 7):
                if (respuesta[f'lugar{i}'] != lugares_correctos[i-1] or
                    respuesta[f'motivo{i}'] != motivos_correctos[i-1] or
                    respuesta[f'orden{i}'] != orden_correcto[i-1]):
                    correctas = False
                    break
            
            if correctas:
                status = 'success'
                form.save()  # Guarda la respuesta en la base de datos
            else:
                status = 'error'
                form.save() 
    else:
        form = RespuestaFormularioForm()
    
    return render(request, 'core/formulario.html', {'form': form, 'status': status})




def destino_final(request):
    status = None
    if request.method == 'POST':
        form = RespuestaDestinoFinalForm(request.POST)
        if form.is_valid():
            respuesta = form.cleaned_data
            
            respuestas_correctas = {'teatro': 'Regina', 'avenida': 'Libertad', 'numero': '1070'}
            
            if (respuesta['teatro'] == respuestas_correctas['teatro'] and
                respuesta['avenida'] == respuestas_correctas['avenida'] and
                respuesta['numero'] == respuestas_correctas['numero']):
                status = 'success'
                form.save()  # Guarda la respuesta en la base de datos
            else:
                status = 'error'
                form.save() 
    else:
        form = RespuestaDestinoFinalForm()
    
    return render(request, 'core/destinofinal.html', {'form': form, 'status': status})

def juego(request):
    return render(request, "core/juego.html")

def pista1(request):
    return render(request, "core/pista1.html")

def pista2(request):
    return render(request, "core/pista2.html")

def pista3(request):
    return render(request, "core/pista3.html")

def pista4(request):
    return render(request, "core/pista4.html")

def pista5(request):
    return render(request, "core/pista5.html")

def pista6(request):
    return render(request, "core/pista6.html")

def descanso(request):
    return render(request, "core/descanso.html")








