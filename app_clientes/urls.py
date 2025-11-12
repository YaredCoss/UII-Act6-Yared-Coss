from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_agencia, name='inicio_agencia'),
    path('clientes/agregar/', views.agregar_clientes, name='agregar_clientes'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/editar/<int:cliente_id>/', views.actualizar_clientes, name='actualizar_clientes'),
    path('clientes/editar/guardar/<int:cliente_id>/', views.realizar_actualizacion_clientes, name='realizar_actualizacion_clientes'),
    path('clientes/borrar/<int:cliente_id>/', views.borrar_clientes, name='borrar_clientes'),

    path('transportes/agregar/', views.agregar_transportes, name='agregar_transportes'),
    path('transportes/', views.ver_transportes, name='ver_transportes'),
    path('transportes/editar/<int:transporte_id>/', views.actualizar_transportes, name='actualizar_transportes'),
    path('transportes/editar/guardar/<int:transporte_id>/', views.realizar_actualizacion_transportes, name='realizar_actualizacion_transportes'),
    path('transportes/borrar/<int:transporte_id>/', views.borrar_transportes, name='borrar_transportes'),

    path('viajes/agregar/', views.agregar_viajes, name='agregar_viajes'),
    path('viajes/', views.ver_viajes, name='ver_viajes'),
    path('viajes/editar/<int:viaje_id>/', views.actualizar_viajes, name='actualizar_viajes'),
    path('viajes/editar/guardar/<int:viaje_id>/', views.realizar_actualizacion_viajes, name='realizar_actualizacion_viajes'),
    path('viajes/borrar/<int:viaje_id>/', views.borrar_viajes, name='borrar_viajes'),

    # Alojamiento
    path('alojamiento/agregar/', views.agregar_alojamiento, name='agregar_alojamiento'),
    path('alojamiento/', views.ver_alojamiento, name='ver_alojamiento'),
    path('alojamiento/editar/<int:id>/', views.actualizar_alojamiento, name='actualizar_alojamiento'),
    path('alojamiento/editar/guardar/<int:id>/', views.realizar_actualizacion_alojamiento, name='realizar_actualizacion_alojamiento'),
    path('alojamiento/borrar/<int:id>/', views.borrar_alojamiento, name='borrar_alojamiento'),

    # Empleado
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/editar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/editar/guardar/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
]