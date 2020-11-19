from django.db import models
from django.conf import settings
from django.utils import timezone

class Vendedor(models.Model):
    """Modelo de Vendedor"""
    nombre = models.CharField(max_length=100)
    agregado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Regresar el nombre"""
        return self.nombre


class Productos(models.Model):
    proveedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    nomprod=models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descrip = models.TextField(blank=True)
    agregado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Regresar el nombre"""
        return self.nomprod