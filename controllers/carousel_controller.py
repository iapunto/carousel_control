"""
Controlador para el carrusel vertical de almacenamiento.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-13
"""

from models.plc_simulator import PLCSimulator
from commons.utils import interpretar_estado_plc
import time

class CarouselController:
    def __init__(self, plc):
        self.plc = plc

    def send_command(self, command, argument=None):
        if self.plc.connect():
            full_command = f"{argument} {command}" if argument is not None else command 
            
            # Lee el estado y la posición del PLC            
            response = self.plc.send_command_and_receive_response(full_command) 

            if response:
                # Muestra el estado en formato binario de 8 bits
                binary_status = format(response['status_code'], '08b')
                print(f"Estado actual del PLC (binario): {binary_status}")
                # Interpreta el estado del PLC
                estados_plc = interpretar_estado_plc(response['status_code'])
                for nombre_estado, descripcion in estados_plc.items():
                    print(f"{nombre_estado}: {descripcion}")

                # Muestra la posición escalada en formato binario de 8 bits
                binary_position = format(response['position']) 
                print(f"Posición actual del carrusel: {binary_position}")

                # ... (resto de la lógica para verificar el estado y enviar el comando)
            
            #time.sleep(1)
            self.plc.close()
        else:
            print("No se pudo conectar al PLC. Verifica la configuración.")