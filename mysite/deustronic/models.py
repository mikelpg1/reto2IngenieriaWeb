from django.db import models
from datetime import datetime
# Create your models here.
class Componente(models.Model):
    referencia = models.CharField(max_length=45, primary_key=True)
    nombre = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    imagen = models.ImageField(upload_to='deustronic/static/img/componentes', blank = True, null =False, verbose_name='imagen')
    
    def __str__(self):
        return self.nombre
   
class Producto(models.Model):
    referencia = models.CharField(max_length=45, primary_key=True)
    nombre = models.CharField(max_length = 45)
    categoria = models.CharField(max_length=25)
    componente = models.ManyToManyField(Componente)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to = 'deustronic/static/img/productos', blank = True, null = True, verbose_name='imagen')
    
    def __str__(self):
        return self.producto_nombre
    
class Cliente(models.Model):
    CIF = models.CharField(max_length=9, primary_key=True)
    nombreEmpresa = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    datosContacto = models.CharField(max_length= 45)
    
    def __str__(self):
        return self.nombreEmpresa

class Pedido(models.Model):
    referencia = models.CharField(max_length=45, primary_key=True)
    fecha = models.DateField(auto_now = True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = True)
    producto = models.ManyToManyField(Producto)
    cantidadproducto = models.IntegerField()
    precioTotal = models.FloatField()
    
    def __str__(self):
        return self.referencia