"""
Proyecto de Control de Carrusel Vertical

Este script principal es el punto de entrada del programa de control de carrusel. 
Se encarga de cargar la configuración, establecer la conexión con el PLC, 
crear el controlador y enviar comandos de ejemplo.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-13
"""

from dotenv import load_dotenv
import os
import time

from models.plc_simulator import PLCSimulator
from controllers.carousel_controller import CarouselController

def main():
    load_dotenv()

    plc_ip = os.getenv('PLC_IP')
    plc_port = int(os.getenv('PLC_PORT'))

    plc = PLCSimulator(plc_ip, plc_port)
    controller = CarouselController(plc)

    # Ejemplo de uso: envía un comando simple y espera la respuesta
    controller.send_command(6,0)

if __name__ == "__main__":
    main()