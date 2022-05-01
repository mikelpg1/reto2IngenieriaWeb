from django.db import models
from datetime import datetime
# Create your models here.


class Componente(models.Model):
    ID = models.CharField(max_length=9, primary_key= True)
    nombre = models.CharField(max_length = 50)
    unidades = models.CharField(max_length=45)
    descripcion = models.CharField(max_length = 100)
  
    
    def __str__(self):
        return self.nombre
   
class Producto(models.Model):
    ID = models.CharField(max_length=9, primary_key= True)
    DNI = models.CharField(max_length=9)
    nombre = models.CharField(max_length = 45)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=25)
    precio = models.FloatField()
    
    def __str__(self):
        return self.producto_nombre
    
class Cliente(models.Model):
    ID = models.CharField(max_length=9, primary_key= True)
    DNI = models.CharField(max_length=9)
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    email = models.EmailField
    telefono = models.IntegerField

    
    def __str__(self):
        return self.nombreEmpresa

class Pedido(models.Model):
    ID = models.CharField(max_length=9, primary_key= True)
    fecha = models.DateField(auto_now = True)
    descripcion = models.CharField(max_length=255)

    
    def __str__(self):
        return self.referencia