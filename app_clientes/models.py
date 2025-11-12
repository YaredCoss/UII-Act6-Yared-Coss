from django.db import models

# ==========================================
# MODELO: clientes
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
# ==========================================

# ==========================================
# MODELO: empleado
# ==========================================
class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=255)
    apellido_empleado = models.CharField(max_length=255)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_empleado}"
# ==========================================

# ==========================================
# MODELO: alojamiento
# ==========================================
class Alojamiento(models.Model):
    nombre_alojamiento = models.CharField(max_length=255)
    descripcion = models.TextField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    paginaweb = models.URLField()

    def __str__(self):
        return self.nombre_alojamiento
# ==========================================

# ==========================================
# MODELO: transporte
# ==========================================
class Transporte(models.Model):
    nombre_transporte = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    horario = models.TimeField()
    empresa = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nombre_transporte
# ==========================================

# ==========================================
# MODELO: viaje
# ==========================================
class Viaje(models.Model):
    nombre_viaje = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    destino = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    clientes = models.ManyToManyField(Cliente, through='ClientesViajes')

    def __str__(self):
        return self.nombre_viaje
# ==========================================

# ==========================================
# MODELO: clientes_viajes
# ==========================================
class ClientesViajes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cliente', 'viaje')

    def __str__(self):
        return f"{self.cliente} - {self.viaje}"
# ==========================================
