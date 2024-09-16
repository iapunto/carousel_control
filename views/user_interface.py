import tkinter as tk
from tkinter import messagebox
from commons.utils import interpretar_estado_plc


class CarouselControlGUI:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Control de Carrusel")

        # Botones de flecha
        up_button = tk.Button(self.window, text="▲", command=self.move_up)
        up_button.pack()

        down_button = tk.Button(self.window, text="▼", command=self.move_down)
        down_button.pack()

        # Selección de cangilón
        bucket_label = tk.Label(self.window, text="Cangilón:")
        bucket_label.pack()

        self.bucket_entry = tk.Entry(self.window)
        self.bucket_entry.pack()

        # Botones de control
        stop_button = tk.Button(self.window, text="Parar", command=self.stop)
        stop_button.pack()

        home_button = tk.Button(
            self.window, text="Ir a Casa", command=self.go_home)
        home_button.pack()

        # Iconos de conexión y configuración (puedes usar imágenes o texto)
        # Ejemplo con un círculo verde
        connect_icon = tk.Label(self.window, text="⬤")
        connect_icon.pack()

        config_button = tk.Button(
            self.window, text="⚙", command=self.open_config)
        config_button.pack()

        # Estado del PLC (inicialmente vacío)
        self.status_label = tk.Label(self.window, text="Estado del PLC:")
        self.status_label.pack()

        self.update_status()  # Actualizar el estado al inicio

        self.window.mainloop()

    def move_up(self):
        self.controller.send_command(
            1, self.bucket_entry.get())  # Comando 1 para MUEVETE

    def move_down(self):
        # Implementa la lógica para mover hacia abajo (si es necesario)
        pass

    def stop(self):
        # Implementa la lógica para detener el carrusel
        pass

    def go_home(self):
        # Implementa la lógica para ir a la posición inicial
        pass

    def open_config(self):
        # Abre un formulario para configurar la IP y el puerto (implementar más adelante)
        pass

    def update_status(self):
        response = self.controller.plc.send_command_and_receive_response(
            "STATUS")
        if response:
            estados_plc = interpretar_estado_plc(response['status_code'])
            status_text = "\n".join(
                [f"{nombre}: {descripcion}" for nombre, descripcion in estados_plc.items()])
            self.status_label.config(text=f"Estado del PLC:\n{status_text}")
        else:
            self.status_label.config(text="Error al obtener el estado del PLC")

        # Actualizar cada 1 segundo
        self.window.after(1000, self.update_status)
