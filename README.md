# Proyecto de Control de Carrusel Vertical

Este proyecto implementa un sistema de control remoto para un carrusel vertical de almacenamiento por cangilones utilizando comunicación por sockets en Python.

## Descripción

El sistema permite enviar comandos al PLC para controlar el movimiento del carrusel y recibir información sobre su estado y posición actual. Utiliza una arquitectura MVC (Modelo-Vista-Controlador) para organizar el código y facilitar su mantenimiento y escalabilidad.

## Características

* Comunicación con el PLC a través de sockets TCP/IP.
* Envío y recepción de comandos y respuestas codificados en UTF-8.
* Verificación del estado del PLC antes de enviar comandos.
* Interpretación de los estados del PLC en formato binario.
* Lectura de la posición actual del carrusel.
* Simulación del comportamiento del PLC para pruebas sin hardware.

## Requisitos

* Python 3.x
* Biblioteca `python-dotenv`
* Biblioteca `socket` (incluida en la biblioteca estándar de Python)

## Instalación

1. Clona este repositorio: `git clone <URL_DEL_REPOSITORIO>`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual:
   * Windows: `venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`

## Configuración

* Crea un archivo `.env` en la raíz del proyecto con la siguiente información:
PLC_IP=192.168.1.100  # Reemplaza con la IP real de tu PLC
PLC_PORT=2000         # Reemplaza con el puerto real del PLC

## Ejecución

* Ejecuta el script principal: `python main.py`

## Autoría

* Desarrollado por: IA Punto: Soluciones Integrales de Tecnología y Marketing
* Proyecto para: INDUSTRIAS PICO S.A.S
* Dirección: MEng. Sergio Lankaster Rondón Melo
* Colaboración: Ing. Francisco Garnica

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
