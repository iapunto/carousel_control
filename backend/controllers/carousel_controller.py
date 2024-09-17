"""
Controlador para el carrusel vertical de almacenamiento.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2023-09-13
Última modificación: 2024-09-16
"""

from models.plc import PLC
from commons.utils import interpretar_estado_plc
import time
import importlib

class CarouselController:
    """
    Maneja la lógica de control del carrusel, incluyendo el envío de comandos y la interpretación de respuestas del PLC.
    """

    def __init__(self, plc):
        """
        Inicializa el controlador con una instancia de la clase PLC.
        """
        self.plc = plc

    def send_command(self, command, argument=None):
        if self.plc.connect():
            # Envía el comando 0 (STATUS) para obtener el estado actual
            self.plc.send_command(0)
            time.sleep(0.2)

            # Lee el estado del PLC
            response = self.plc.receive_response()

            if response:
                # Interpreta y muestra el estado del PLC
                self.print_plc_status(response['status_code'])

                # Muestra la posición del carrusel
                print(f"Posición actual del carrusel: {response['position']}")

                # Verifica si el PLC está en el estado adecuado para moverse
                if self.is_plc_ready_to_move(response['status_code']):
                    if command == 1:  # Comando MUEVETE
                        try:
                            target_position = int(argument)
                            if 0 <= argument <= 9:
                                # Envía el comando de movimiento y luego el argumento
                                #self.plc.send_command(command)
                                full_command = bytes([command, target_position])
                                self.plc.send_command(full_command)
                                time.sleep(0.5) 
                                #self.plc.send_argument(target_position)

                                # Recibe la respuesta al comando MUEVETE (si es necesario)
                                move_response = self.plc.receive_response()
                                if move_response:
                                    print(f"Respuesta al comando MUEVETE: {move_response}")

                            else:
                                print("Error: Número de bucket inválido.")
                        except ValueError:
                            print("Error: Argumento inválido para el comando MUEVETE.")
                    # ... (otros comandos)
                    else:
                        # Para otros comandos, envía el comando y recibe la respuesta directamente
                        self.plc.send_command(command)
                        response = self.plc.receive_response()
                        if response:
                            print(f"Respuesta al comando {command}: {response}")
                        else:
                            print(f"No se recibió respuesta al comando {command}.")

                else:
                    print("El PLC no está en el estado adecuado para moverse.")

            self.plc.close()
        else:
            print("No se pudo conectar al PLC. Verifica la configuración.")


    def monitor_plc_status(self):
        """
        Monitorea continuamente el estado del PLC y lo muestra en la consola.
        """

        if self.plc.connect():
            try:
                while True:
                    # Lee el estado y la posición del PLC
                    self.plc.send_command(0) # Envía el comando 0 para obtener el estado
                    response = self.plc.receive_response()

                    if response:
                        # Interpreta y muestra el estado del PLC
                        self.print_plc_status(response['status_code'])

                        # Muestra la posición
                        print(f"Posición actual del carrusel: {response['position']}")

                    # time.sleep(1)

            except KeyboardInterrupt:
                print("Monitoreo detenido por el usuario.")

            finally:
                self.plc.close()
        else:
            print("No se pudo conectar al PLC. Verifica la configuración.")

    def print_plc_status(self, status_code):
        """
        Imprime el estado del PLC de forma legible.
        """
        estados_plc = interpretar_estado_plc(status_code)
        print(f"Estado del PLC (binario): {format(status_code, '08b')}")
        for nombre_estado, descripcion in estados_plc.items():
            print(f"{nombre_estado}: {descripcion}")

    def is_plc_ready_to_move(self, status_code):
        """
        Verifica si el PLC está en el estado adecuado para moverse.
        """
        estados_plc = interpretar_estado_plc(status_code)
        return estados_plc['READY'] == 'El equipo está listo para operar' and \
               estados_plc['RUN'] == 'El equipo está detenido' and \
               estados_plc['MODO_OPERACION'] == 'Remoto' and \
               estados_plc['ALARMA'] == 'No hay alarma' and \
               estados_plc['PARADA_EMERGENCIA'] == 'Sin parada de emergencia' and \
               estados_plc['VFD'] == 'El variador de velocidad está OK' and \
               estados_plc['ERROR_POSICIONAMIENTO'] == 'No hay error de posicionamiento'