"""
Funciones de utilidad para el proyecto de control de carrusel.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-14
"""

ESTADOS_PLC = {
    0: {
        'nombre': 'READY',
        0: 'El equipo no puede operar',
        1: 'El equipo está listo para operar'
    },
    1: {
        'nombre': 'RUN',
        0: 'El equipo está detenido',
        1: 'El equipo está en movimiento (comando de movimiento activo)'
    },
    2: {
        'nombre': 'MODO_OPERACION',
        0: 'Manual',
        1: 'Automático'
    },
    3: {
        'nombre': 'ALARMA',
        0: 'No hay alarma',
        1: 'Alarma activa'
    },
    4: {
        'nombre': 'PARADA_EMERGENCIA',
        0: 'Sin parada de emergencia',
        1: 'Parada de emergencia presionada y activa'
    },
    5: {
        'nombre': 'VFD',
        0: 'Error en el variador de velocidad',
        1: 'El variador de velocidad está OK'
    },
    6: {
        'nombre': 'ERROR_POSICIONAMIENTO',
        0: 'No hay error de posicionamiento',
        1: 'Ha ocurrido un error en el posicionamiento'
    },
    7: {
        'nombre': 'SENTIDO_GIRO',
        0: 'Ascendente',
        1: 'Descendente'
    }
}

"""
  Interpreta el código de estado del PLC y devuelve un diccionario con los estados y sus descripciones.

  Args:
      status_code: El código de estado del PLC en formato entero (8 bits).

  Returns:
      Un diccionario donde las claves son los nombres de los estados y los valores son sus descripciones.
"""
def interpretar_estado_plc(status_code):

  estado_binario = format(status_code, '08b')
  estados_activos = {}

  for i, bit in enumerate(estado_binario):
      bit_value = int(bit)
      estado = ESTADOS_PLC[i]
      estados_activos[estado['nombre']] = estado[bit_value]

  return estados_activos