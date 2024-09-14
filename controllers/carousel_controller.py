from models.plc import PLC
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

                # Muestra la posición escalada en formato binario de 8 bits
                binary_position = format(response['position_code']) 
                print(f"Posición actual del carrusel (binario): {binary_position}")

                # ... (resto de la lógica para verificar el estado y enviar el comando)
            
            #time.sleep(1)
            self.plc.close()
        else:
            print("No se pudo conectar al PLC. Verifica la configuración.")