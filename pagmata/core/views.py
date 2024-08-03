from django.shortcuts import render, redirect
from .forms import RespuestaFormularioForm, RespuestaDestinoFinalForm

def home(request):
    return render(request, "core/home.html")

def index(request):
    return render(request, "core/index.html")

def turismo(request):
    return render(request, "core/turismo.html")

def formulario(request):
    status = ''
    form = RespuestaFormularioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            respuestas_usuario = form.cleaned_data

            # Respuestas correctas para Formulario
            lugares_correctos = ["Monroe", "Parque Centenario", "Planetario", "Abasto", "Billares 36", "CNBA"]
            motivos_correctos = ["Abrazo", "Beso", "Salidas", "Películas", "Juegos", "Nos conocimos"]
            orden_correcto = [5, 6, 3, 4, 2, 1]

            if ([
                respuestas_usuario['lugar1'], respuestas_usuario['lugar2'], respuestas_usuario['lugar3'],
                respuestas_usuario['lugar4'], respuestas_usuario['lugar5'], respuestas_usuario['lugar6']
            ] == lugares_correctos and
                [
                    respuestas_usuario['motivo1'], respuestas_usuario['motivo2'], respuestas_usuario['motivo3'],
                    respuestas_usuario['motivo4'], respuestas_usuario['motivo5'], respuestas_usuario['motivo6']
                ] == motivos_correctos and
                [
                    respuestas_usuario['orden1'], respuestas_usuario['orden2'], respuestas_usuario['orden3'],
                    respuestas_usuario['orden4'], respuestas_usuario['orden5'], respuestas_usuario['orden6']
                ] == orden_correcto):

                # Guardar las respuestas en la base de datos
                form.save()

                status = 'success'
            else:
                status = 'error'

    return render(request, 'core/formulario.html', {'form': form, 'status': status})

def destino_final(request):
    status = ''
    form = RespuestaDestinoFinalForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            respuestas_destino = form.cleaned_data

            respuestas_correctas = {'teatro': 'Regina', 'avenida': 'Libertad', 'numero': '1070'}

            if (respuestas_destino['teatro'] == respuestas_correctas['teatro'] and
                respuestas_destino['avenida'] == respuestas_correctas['avenida'] and
                respuestas_destino['numero'] == respuestas_correctas['numero']):

                # Guardar las respuestas en la base de datos
                form.save()

                status = 'success'
            else:
                status = 'error'

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
