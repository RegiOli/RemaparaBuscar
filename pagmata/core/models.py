from django.db import models

class RespuestaFormulario(models.Model):
    lugar1 = models.CharField(max_length=100)
    lugar2 = models.CharField(max_length=100)
    lugar3 = models.CharField(max_length=100)
    lugar4 = models.CharField(max_length=100)
    lugar5 = models.CharField(max_length=100)
    lugar6 = models.CharField(max_length=100)
    motivo1 = models.CharField(max_length=100)
    motivo2 = models.CharField(max_length=100)
    motivo3 = models.CharField(max_length=100)
    motivo4 = models.CharField(max_length=100)
    motivo5 = models.CharField(max_length=100)
    motivo6 = models.CharField(max_length=100)
    orden1 = models.IntegerField()
    orden2 = models.IntegerField()
    orden3 = models.IntegerField()
    orden4 = models.IntegerField()
    orden5 = models.IntegerField()
    orden6 = models.IntegerField()

class RespuestaDestinoFinal(models.Model):
    teatro = models.CharField(max_length=100)
    avenida = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
