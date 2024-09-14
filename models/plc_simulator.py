import time
import random

class PLCSimulator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.current_position = random.randint(0, 9) 
        self.is_running = False  # Estado inicial: detenido
        self.status_code = 0  # Initialize status_code to a default value

    # ... (resto del código)

    def connect(self):
        print("Simulando conexión con el PLC...")
        return True

    def close(self):
        print("Simulando cierre de conexión con el PLC...")

    def send_command_and_receive_response(self, command):
        print(f"Comando recibido en el simulador: {command}")
        time.sleep(1)

        if command == "STATUS":
            return {'status_code': self.status_code, 'position': self.current_position}

        elif command.startswith("MUEVETE"):
            try:
                _, target_position = command.split()
                target_position = int(target_position)

                # Simula el movimiento del carrusel
                if not self.is_running:  # Solo se mueve si no está ya en movimiento
                    self.is_running = True
                    self.current_status |= 0b00000010  # Enciende el bit 1 (RUN)
                    print(f"Moviendo el carrusel a la posición {target_position}...")
                    time.sleep(2)
                    self.current_position = target_position
                    self.is_running = False
                    self.current_status &= 0b11111101  # Apaga el bit 1 (RUN)

                return {'status_code': self.current_status, 'position': self.current_position}
            except ValueError:
                return "Error: Argumento inválido para el comando MUEVETE"

        else:
            # Genera un nuevo estado aleatorio para cualquier otro comando
            self.status_code = random.randint(0, 255) 
            return {'status_code': self.status_code, 'position': self.current_position}