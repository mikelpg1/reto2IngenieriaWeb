from django.contrib import admin
from .models import Pedido, Producto, Componente, Cliente

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Cliente)

# Register your models here.
