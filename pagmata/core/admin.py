from django.contrib import admin
from .models import RespuestaFormulario, RespuestaDestinoFinal
from .models import Respuesta

admin.site.register(RespuestaFormulario)
admin.site.register(RespuestaDestinoFinal)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'jugar', 'caminar', 'num1')

admin.site.register(Respuesta, RespuestaAdmin)
