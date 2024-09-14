from dotenv import load_dotenv
import os
import time

from models.plc import PLC
from controllers.carousel_controller import CarouselController

def main():
    load_dotenv()

    plc_ip = os.getenv('PLC_IP')
    plc_port = int(os.getenv('PLC_PORT'))

    plc = PLC(plc_ip, plc_port)
    controller = CarouselController(plc)

    # Ejemplo de uso: envía un comando simple y espera la respuesta
    controller.send_command(6,0)
    time.sleep(3)
    controller.send_command(6,1)


if __name__ == "__main__":
    main()