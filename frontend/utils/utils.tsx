// Definir una interfaz para representar la estructura de ESTADOS_PLC
interface EstadoPLC {
    nombre: string;
    0: string;
    1: string;
  }
  
  // Definir un tipo para el diccionario de estados
  type EstadosPLCDictionary = {
    [key in 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7]: EstadoPLC; 
  }
  
  export const ESTADOS_PLC: EstadosPLCDictionary = {
    0: {
      nombre: 'READY',
      0: 'El equipo no puede operar',
      1: 'El equipo está listo para operar'
    },
    1: {
      nombre: 'RUN',
      0: 'El equipo está detenido',
      1: 'El equipo está en movimiento (comando de movimiento activo)'
    },
    2: {
      nombre: 'MODO_OPERACION',
      0: 'Remoto',
      1: 'Manual'
    },
    3: {
      nombre: 'ALARMA',
      0: 'No hay alarma',
      1: 'Alarma activa'
    },
    4: {
      nombre: 'PARADA_EMERGENCIA',
      0: 'Sin parada de emergencia',
      1: 'Parada de emergencia presionada y activa'
    },
    5: {
      nombre: 'VFD',
      0: 'El variador de velocidad está OK',
      1: 'Error en el variador de velocidad'
    },
    6: {
      nombre: 'ERROR_POSICIONAMIENTO',
      0: 'No hay error de posicionamiento',
      1: 'Ha ocurrido un error en el posicionamiento'
    },
    7: {
      nombre: 'SENTIDO_GIRO',
      0: 'Ascendente',
      1: 'Descendente'
    }
  };
  
  export function interpretarEstadoPLC(statusCode: number): { [key: string]: string } {
    const estadoBinario = statusCode.toString(2).padStart(8, '0'); 
    const estadosActivos: { [key: string]: string } = {};
  
    for (let i = 0; i < 8; i++) {
      const bitValue = (statusCode >> i) & 1; 
      const estado = ESTADOS_PLC[i]; 
      estadosActivos[estado.nombre] = estado[bitValue]; 
    }
  
    return estadosActivos;
  }