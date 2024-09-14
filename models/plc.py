"""
Clase PLC para la comunicación con el PLC Delta AS Series a través de sockets.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-13
"""

# ... (resto del código)

import socket
import struct

class PLC:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            return True
        except ConnectionRefusedError:
            print(f"Error: No se pudo establecer la conexión con el PLC en {self.ip}:{self.port}.")
            return False

    def close(self):
        if self.sock:
            self.sock.close()

    def send_command_and_receive_response(self, command):
        # Codifica el comando (ajusta según el protocolo del PLC)
        encoded_command = command.encode('utf-8')

        # Envía el comando
        self.sock.sendall(encoded_command)

        # Recibe la respuesta (asumiendo 1 byte para estado y 2 para posición)
        status_data = self.sock.recv(1)
        position_data = self.sock.recv(4) 

        if status_data and position_data:
            status_code = status_data[0]
            position_code = struct.unpack('>HH', position_data)  # Desempaqueta la posición (16 bits, big-endian)

            return {
                'status_code': status_code,
                'position_code': position_code
            }
        else:
            print("No se recibió respuesta completa del PLC.")
            return None