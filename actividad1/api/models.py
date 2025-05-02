from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    descripcion = models.TextField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='gastos')
    def __str__(self):
        return f"{self.descripcion} - {self.importe}"

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    personas = models.ManyToManyField(Persona, related_name='grupos')
    def __str__(self):
        return self.nombre
