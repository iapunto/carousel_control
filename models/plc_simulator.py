"""
Clase PLC para SIMULAR la comunicación con el PLC Delta AS Series a través de sockets.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-14
"""

import time
import random

class PLCSimulator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.current_position = random.randint(1,10)  # Posición inicial del carrusel

    def connect(self):
        print("Simulando conexión con el PLC...")
        return True

    def close(self):
        print("Simulando cierre de conexión con el PLC...")

    def send_command_and_receive_response(self, command):
        print(f"Comando recibido en el simulador: {command}")
        time.sleep(1)  # Simula un pequeño retraso en la respuesta

        # Lógica para simular la respuesta del PLC
        if command == "STATUS":
            return {'status_code': 1, 'position': self.current_position}
        elif command.startswith("MUEVETE"):
            try:
                _, target_position = command.split()  # Separa el comando y el argumento
                target_position = int(target_position)
                
                # Simula el movimiento del carrusel
                print(f"Moviendo el carrusel a la posición {target_position}...")
                time.sleep(2)  # Simula el tiempo de movimiento
                self.current_position = target_position
                
                return {'status_code': 1, 'position': self.current_position}
            except ValueError:
                return "Error: Argumento inválido para el comando MUEVETE"
        else:
            return {'status_code': 0, 'position': self.current_position}  # Comando no reconocido