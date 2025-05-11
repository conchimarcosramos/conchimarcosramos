from django.db import models
from django.utils.timezone import now  # ✅ Importación correcta

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Ajuste para mayor claridad
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    personas = models.ManyToManyField(Persona, related_name='grupos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class GastoManager(models.Manager):
    """Manager personalizado para filtrar gastos grandes"""
    
    def gastos_grandes(self, minimo=100):
        return self.filter(importe__gte=minimo)

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Usamos `auto_now_add=True` para consistencia
    updated_at = models.DateTimeField(auto_now=True)

    objects = GastoManager()  # 🔹 Activamos el manager personalizado

    def __str__(self):
        return f"{self.descripcion} - {self.importe}€"