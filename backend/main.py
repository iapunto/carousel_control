"""
Proyecto de Control de Carrusel Vertical

Este script principal es el punto de entrada del programa de control de carrusel. 
Se encarga de cargar la configuración, establecer la conexión con el PLC, 
crear el controlador y la interfaz gráfica.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2023-09-13
Última modificación: 2024-09-16
"""

from dotenv import load_dotenv
import os

from models.plc import PLC
from controllers.carousel_controller import CarouselController

def main():
    """Función principal del programa."""

    load_dotenv()

    plc_ip = os.getenv('PLC_IP')
    plc_port = int(os.getenv('PLC_PORT'))

    plc = PLC(plc_ip, plc_port)
    controller = CarouselController(plc)

    # Crea la interfaz gráfica y pásale el controlador
    #
    # Inicia el monitoreo del estado del PLC en segundo plano (si es necesario)
    # controller.monitor_plc_status()  # Descomenta esta línea si necesitas monitoreo continuo
    controller.send_command(1,4)
    
if __name__ == "__main__":
    
    main()