from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    descripcion = models.CharField(max_length=250, null=False)
    imagen = models.CharField(max_length=2000, null=False)
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return f"Producto  {self.imagen} - {self.titulo} - {self.descripcion} - {self.link}"

class Salud(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    descripcion = models.CharField(max_length=250, null=False)
    imagen = models.CharField(max_length=2000, null=False)
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return f"Salud  {self.imagen} - {self.titulo} - {self.descripcion} - {self.link}"

class Motricidad(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    descripcion = models.CharField(max_length=250, null=False)
    imagen = models.CharField(max_length=2000, null=False)
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return f"Motricidad  {self.imagen} - {self.titulo} - {self.descripcion} - {self.link}"

class Rincon(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    descripcion = models.CharField(max_length=250, null=False)
    imagen = models.CharField(max_length=2000, null=False)
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return f"Rincon  {self.imagen} - {self.titulo} - {self.descripcion} - {self.link}"