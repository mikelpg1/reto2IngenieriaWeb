from django.db import models
from datetime import datetime
# Create your models here.
class Componente(models.Model):
    componente_referencia = models.CharField(max_length=45, primary_key=True)
    componente_nombre = models.CharField(max_length=45)
    componente_marca = models.CharField(max_length=45)
    componente_imagen = models.ImageField(upload_to='deustronic/static/img/componentes', blank = True, null =False, verbose_name='componente_imagen')
    
    def __str__(self):
        return self.componente_nombre
   
class Producto(models.Model):
    producto_referencia = models.CharField(max_length=45, primary_key=True)
    producto_nombre = models.CharField(max_length = 45)
    producto_categoria = models.CharField(max_length=25)
    producto_componente = models.ManyToManyField(Componente)
    producto_descripcion = models.CharField(max_length=255)
    producto_precio = models.FloatField()
    producto_imagen = models.ImageField(upload_to = 'deustronic/static/img/productos', blank = True, null = True, verbose_name='producto_imagen')
    
    def __str__(self):
        return self.producto_nombre
    
class Cliente(models.Model):
    cliente_CIF = models.CharField(max_length=9, primary_key=True)
    cliente_nombreEmpresa = models.CharField(max_length=45)
    cliente_direccion = models.CharField(max_length=45)
    clientw_datosContacto = models.CharField(max_length= 45)
    
    def __str__(self):
        return self.cliente_nombreEmpresa

class Pedido(models.Model):
    pedido_referencia = models.CharField(max_length=45, primary_key=True)
    pedido_fecha = models.DateField(auto_now = True)
    pedido_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = True)
    pedido_producto = models.ManyToManyField(Producto)
    pedido_cantidadproducto = models.IntegerField()
    pedido_precioTotal = models.FloatField()
    
    def __str__(self):
        return self.pedido_referencia