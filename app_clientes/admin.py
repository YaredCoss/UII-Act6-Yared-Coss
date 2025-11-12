from django.contrib import admin
from .models import Cliente, Empleado, Alojamiento, Transporte, Viaje, ClientesViajes

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Alojamiento)
admin.site.register(Transporte)
admin.site.register(Viaje)
admin.site.register(ClientesViajes)
