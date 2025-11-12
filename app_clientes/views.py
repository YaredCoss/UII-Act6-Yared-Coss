from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Cliente, Empleado, Alojamiento, Transporte, Viaje

# ====================================================
# INICIO
# ====================================================
def inicio_agencia(request):
    return render(request, 'inicio.html')


# ====================================================
# CRUD CLIENTES
# ====================================================
def agregar_clientes(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre', '').strip(),
            apellido=request.POST.get('apellido', '').strip(),
            correo=request.POST.get('correo') or None,
            telefono=request.POST.get('telefono') or None,
            direccion=request.POST.get('direccion') or None,
            fecha_nacimiento=request.POST.get('fecha_nacimiento') or None
        )
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_clientes.html')


def ver_clientes(request):
    busqueda = request.GET.get('busqueda', '')
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda)
    ).order_by('apellido', 'nombre')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes, 'busqueda': busqueda})


def actualizar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})


def realizar_actualizacion_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.correo = request.POST.get('correo') or None
        cliente.telefono = request.POST.get('telefono') or None
        cliente.direccion = request.POST.get('direccion') or None
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_clientes', cliente_id=cliente.pk)


def borrar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})


# ====================================================
# CRUD EMPLEADOS
# ====================================================
def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre_empleado=request.POST.get('nombre_empleado', '').strip(),
            apellido_empleado=request.POST.get('apellido_empleado', '').strip(),
            puesto=request.POST.get('puesto') or None,
            salario=request.POST.get('salario') or None,
            telefono=request.POST.get('telefono') or None,
            correo=request.POST.get('correo') or None
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')


def ver_empleado(request):
    busqueda = request.GET.get('busqueda', '')
    empleados = Empleado.objects.filter(
        Q(nombre_empleado__icontains=busqueda) |
        Q(apellido_empleado__icontains=busqueda) |
        Q(puesto__icontains=busqueda)
    ).order_by('apellido_empleado', 'nombre_empleado')
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados, 'busqueda': busqueda})


def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})


def realizar_actualizacion_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        empleado.nombre_empleado = request.POST.get('nombre_empleado', empleado.nombre_empleado)
        empleado.apellido_empleado = request.POST.get('apellido_empleado', empleado.apellido_empleado)
        empleado.puesto = request.POST.get('puesto') or None
        empleado.salario = request.POST.get('salario') or None
        empleado.telefono = request.POST.get('telefono') or None
        empleado.correo = request.POST.get('correo') or None
        empleado.save()
        return redirect('ver_empleado')
    return redirect('actualizar_empleado', id=empleado.pk)


def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# ====================================================
# CRUD ALOJAMIENTOS
# ====================================================
def agregar_alojamiento(request):
    if request.method == 'POST':
        Alojamiento.objects.create(
            nombre_alojamiento=request.POST.get('nombre_alojamiento', '').strip(),
            descripcion=request.POST.get('descripcion') or None,
            direccion=request.POST.get('direccion') or None,
            telefono=request.POST.get('telefono') or None,
            precio=request.POST.get('precio') or None,
            calificacion=request.POST.get('calificacion') or None,
            paginaweb=request.POST.get('paginaweb') or None
        )
        return redirect('ver_alojamiento')
    return render(request, 'alojamiento/agregar_alojamiento.html')


def ver_alojamiento(request):
    busqueda = request.GET.get('busqueda', '')
    alojamientos = Alojamiento.objects.filter(
        Q(nombre_alojamiento__icontains=busqueda) |
        Q(descripcion__icontains=busqueda) |
        Q(telefono__icontains=busqueda)
    ).order_by('nombre_alojamiento')
    return render(request, 'alojamiento/ver_alojamiento.html', {'alojamientos': alojamientos, 'busqueda': busqueda})


def actualizar_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, pk=id)
    return render(request, 'alojamiento/actualizar_alojamiento.html', {'alojamiento': alojamiento})


def realizar_actualizacion_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, pk=id)
    if request.method == 'POST':
        alojamiento.nombre_alojamiento = request.POST.get('nombre_alojamiento', alojamiento.nombre_alojamiento)
        alojamiento.descripcion = request.POST.get('descripcion') or None
        alojamiento.direccion = request.POST.get('direccion') or None
        alojamiento.telefono = request.POST.get('telefono') or None
        alojamiento.precio = request.POST.get('precio') or None
        alojamiento.calificacion = request.POST.get('calificacion') or None
        alojamiento.paginaweb = request.POST.get('paginaweb') or None
        alojamiento.save()
        return redirect('ver_alojamiento')
    return redirect('actualizar_alojamiento', id=alojamiento.pk)


def borrar_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, pk=id)
    if request.method == 'POST':
        alojamiento.delete()
        return redirect('ver_alojamiento')
    return render(request, 'alojamiento/borrar_alojamiento.html', {'alojamiento': alojamiento})


# ====================================================
# CRUD TRANSPORTES
# ====================================================
def agregar_transportes(request):
    if request.method == 'POST':
        Transporte.objects.create(
            nombre_transporte=request.POST.get('nombre_transporte', '').strip(),
            descripcion=request.POST.get('descripcion') or None,
            tipo=request.POST.get('tipo') or None,
            capacidad=request.POST.get('capacidad') or None,
            precio=request.POST.get('precio') or None,
            horario=request.POST.get('horario') or None,
            empresa=request.POST.get('empresa') or None
        )
        return redirect('ver_transportes')
    return render(request, 'transportes/agregar_transportes.html')


def ver_transportes(request):
    busqueda = request.GET.get('busqueda', '')
    transportes = Transporte.objects.filter(
        Q(nombre_transporte__icontains=busqueda) |
        Q(tipo__icontains=busqueda) |
        Q(empresa__icontains=busqueda)
    ).order_by('nombre_transporte')
    return render(request, 'transportes/ver_transportes.html', {'transportes': transportes, 'busqueda': busqueda})


def actualizar_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    return render(request, 'transportes/actualizar_transportes.html', {'transporte': transporte})


def realizar_actualizacion_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, pk=transporte_id)
    if request.method == 'POST':
        transporte.nombre_transporte = request.POST.get('nombre_transporte', transporte.nombre_transporte)
        transporte.descripcion = request.POST.get('descripcion') or None
        transporte.tipo = request.POST.get('tipo') or None
        transporte.capacidad = request.POST.get('capacidad') or None
        transporte.precio = request.POST.get('precio') or None
        transporte.horario = request.POST.get('horario') or None
        transporte.empresa = request.POST.get('empresa') or None
        transporte.save()
        return redirect('ver_transportes')
    return redirect('actualizar_transportes', transporte_id=transporte.pk)


def borrar_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    if request.method == 'POST':
        transporte.delete()
        return redirect('ver_transportes')
    return render(request, 'transportes/borrar_transportes.html', {'transporte': transporte})


# ====================================================
# CRUD VIAJES
# ====================================================
def agregar_viajes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    transportes = Transporte.objects.all().order_by('nombre_transporte')
    empleados = Empleado.objects.all().order_by('apellido_empleado', 'nombre_empleado')
    alojamientos = Alojamiento.objects.all().order_by('nombre_alojamiento')

    if request.method == 'POST':
        # Validar que todos los campos obligatorios estén presentes
        empleado_id = request.POST.get('empleado')
        alojamiento_id = request.POST.get('alojamiento')
        transporte_id = request.POST.get('transporte')
        if not empleado_id or not alojamiento_id or not transporte_id:
            # Mostrar error o recargar página
            return render(request, 'viajes/agregar_viajes.html', {
                'clientes': clientes,
                'transportes': transportes,
                'empleados': empleados,
                'alojamientos': alojamientos,
                'error': 'Debe seleccionar empleado, transporte y alojamiento'
            })

        viaje = Viaje.objects.create(
            nombre_viaje=request.POST.get('nombre_viaje', '').strip(),
            destino=request.POST.get('destino', '').strip(),
            descripcion=request.POST.get('descripcion') or None,
            fecha_salida=request.POST.get('fecha_salida') or None,
            fecha_regreso=request.POST.get('fecha_regreso') or None,
            precio=request.POST.get('precio') or None,
            empleado_id=empleado_id,
            alojamiento_id=alojamiento_id,
            transporte_id=transporte_id
        )
        cliente_ids = request.POST.getlist('clientes')
        viaje.clientes.set(cliente_ids)
        return redirect('ver_viajes')

    return render(request, 'viajes/agregar_viajes.html', {
        'clientes': clientes,
        'transportes': transportes,
        'empleados': empleados,
        'alojamientos': alojamientos,
    })

def ver_viajes(request):
    busqueda = request.GET.get('busqueda', '')
    viajes = Viaje.objects.filter(
        Q(nombre_viaje__icontains=busqueda) |
        Q(destino__icontains=busqueda) |
        Q(empleado__nombre_empleado__icontains=busqueda) |
        Q(alojamiento__nombre_alojamiento__icontains=busqueda)
    ).order_by('fecha_salida')
    return render(request, 'viajes/ver_viajes.html', {
        'viajes': viajes,
        'busqueda': busqueda
    })

def actualizar_viajes(request, viaje_id):
    viaje = get_object_or_404(Viaje, pk=viaje_id)
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    transportes = Transporte.objects.all().order_by('nombre_transporte')
    empleados = Empleado.objects.all().order_by('apellido_empleado', 'nombre_empleado')
    alojamientos = Alojamiento.objects.all().order_by('nombre_alojamiento')

    return render(request, 'viajes/actualizar_viajes.html', {
        'viaje': viaje,
        'clientes': clientes,
        'transportes': transportes,
        'empleados': empleados,
        'alojamientos': alojamientos,
    })


def realizar_actualizacion_viajes(request, viaje_id):
    viaje = get_object_or_404(Viaje, pk=viaje_id)
    if request.method == 'POST':
        viaje.nombre_viaje = request.POST.get('nombre_viaje', viaje.nombre_viaje)
        viaje.destino = request.POST.get('destino', viaje.destino)
        viaje.descripcion = request.POST.get('descripcion') or None
        viaje.fecha_salida = request.POST.get('fecha_salida') or None
        viaje.fecha_regreso = request.POST.get('fecha_regreso') or None
        viaje.precio = request.POST.get('precio') or None
        viaje.transporte = Transporte.objects.get(pk=int(request.POST.get('transporte'))) if request.POST.get('transporte') else viaje.transporte
        viaje.empleado = Empleado.objects.get(pk=int(request.POST.get('empleado'))) if request.POST.get('empleado') else viaje.empleado
        viaje.alojamiento = Alojamiento.objects.get(pk=int(request.POST.get('alojamiento'))) if request.POST.get('alojamiento') else viaje.alojamiento
        viaje.save()
        cliente_ids = request.POST.getlist('clientes')
        viaje.clientes.set(cliente_ids)
        return redirect('ver_viajes')

    return redirect('actualizar_viajes', viaje_id=viaje.pk)

def borrar_viajes(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)
    if request.method == 'POST':
        viaje.delete()
        return redirect('ver_viajes')
    return render(request, 'viajes/borrar_viajes.html', {'viaje': viaje})
