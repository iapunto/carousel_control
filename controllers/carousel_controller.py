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
            full_command = f"{argument} {
                command}" if argument is not None else command

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

                # Verifica si el PLC está en el estado adecuado para moverse
                if estados_plc['READY'] == 'El equipo está listo para operar' and \
                   estados_plc['RUN'] == 'El equipo está detenido' and \
                   estados_plc['MODO_OPERACION'] == 'Automático' and \
                   estados_plc['ALARMA'] == 'No hay alarma' and \
                   estados_plc['PARADA_EMERGENCIA'] == 'Sin parada de emergencia' and \
                   estados_plc['VFD'] == 'El variador de velocidad está OK' and \
                   estados_plc['ERROR_POSICIONAMIENTO'] == 'No hay error de posicionamiento' and \
                   estados_plc['SENTIDO_GIRO'] == 'Ascendente':

                    if command == 1:  # Comando MUEVETE
                        try:
                            target_position = int(argument)
                            if 0 <= target_position <= 9:
                                full_command = f"{target_position} 1"
                                response = self.plc.send_command_and_receive_response(
                                    full_command)
                                if response:
                                    print(f"Comando enviado: {full_command}")
                                    time.sleep(1)
                                    print(f"Respuesta del PLC: {response}")
                            else:
                                print("Error: Número de bucket inválido.")
                        except ValueError:
                            print(
                                "Error: Argumento inválido para el comando MUEVETE.")
                    # ... (otros comandos)
                    else:
                        print("Comando no reconocido.")
                else:
                    print("El PLC no está en el estado adecuado para moverse.")

            self.plc.close()
        else:
            print("No se pudo conectar al PLC. Verifica la configuración.")

            # time.sleep(1)
            self.plc.close()
