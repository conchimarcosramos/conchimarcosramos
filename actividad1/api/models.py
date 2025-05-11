from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última modificación

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    personas = models.ManyToManyField(Persona, related_name='grupos')

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Última modificación

    def __str__(self):
        return f"{self.descripcion} - {self.importe}€"


# creo las modificaciones necesarias para que el modelo funcione según el criterio del profesor