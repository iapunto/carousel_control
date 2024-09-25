from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
from models.plc_simulator import PLCSimulator
from models.inventory import Inventory
from controllers.carousel_controller import CarouselController
from controllers.inventory_controller import InventoryController
from controllers.brand_controller import BrandController
from controllers.category_controller import CategoryController
from dotenv import load_dotenv
import os
import time

load_dotenv()

plc_ip = os.getenv('PLC_IP')
plc_port = int(os.getenv('PLC_PORT'))

# Crear instancias de PLC y controlador 
plc = PLCSimulator(plc_ip, plc_port) # plc = PLC(plc_ip, plc_port) si usas el PLC real O plc_simulator = PLCSimulator(plc_ip, plc_port) si usas el Simulador PLC
carousel_controller = CarouselController(plc)

# Crear instancias de los controladores de inventario, marcas y categorías
inventory = Inventory()
inventory_controller = InventoryController(inventory, carousel_controller)
brand_controller = BrandController()
category_controller = CategoryController()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*" }})   # Enable CORS for all routes

@app.route('/v1/command', methods=['POST'])
@cross_origin()
def send_command():
    """
    Envía un comando al PLC.

    POST:
        Envía un comando al PLC.
        Datos esperados en el cuerpo de la solicitud (JSON):
            - command: Número entero que representa el comando a enviar (0-255).
            - argument: Número entero que representa el argumento del comando (opcional, 0-255).
    Respuestas:
        - 200 OK: Mensaje de éxito en formato JSON.
        - 400 Bad Request: Si faltan datos requeridos, los datos son inválidos o el PLC no está en el estado adecuado.
        - 500 Internal Server Error: Si ocurre un error al comunicarse con el PLC.
    """

    if plc.connect():
        try:
            data = request.get_json()
            command = data.get('command')
            argument = data.get('argument')

            if command is not None:
                # Verificar si el comando es válido
                if not isinstance(command, int) or command < 0 or command > 255:
                    return jsonify({'error': 'Comando inválido'}), 400

                if argument is not None:
                    # Verificar si el argumento es válido
                    if not isinstance(argument, int) or argument < 0 or argument > 255:
                        return jsonify({'error': 'Argumento inválido'}), 400

                # Enviar el comando y el argumento al PLC
                carousel_controller.send_command(command, argument)

                return jsonify({'message': 'Comando enviado exitosamente'}), 200
            else:
                return jsonify({'error': 'Comando no especificado'}), 400
        except Exception as e:
            return jsonify({'error': f'Error al comunicarse con el PLC: {e}'}), 500
    else:
        return jsonify({'error': 'No se pudo conectar al PLC'}), 500

@app.route('/v1/status', methods=['GET'])
@cross_origin()
def get_status():
    """
    Obtiene el estado y la posición actual del PLC.

    GET:
        Obtiene el estado y la posición actual del PLC.
    Respuestas:
        - 200 OK: Diccionario con el código de estado ('status_code') y la posición ('position') del PLC en formato JSON.
        - 500 Internal Server Error: Si ocurre un error al comunicarse con el PLC.
    """
    
    # Imprime la URL de origen de la solicitud
    # print(f"Solicitud recibida desde: {request.headers.get('Origin')}")

    if plc.connect():
        try:
            # Envía el comando 0 (STATUS) para obtener el estado actual
            plc.send_command(0)
            time.sleep(0.5)  # Espera para que el PLC procese el comando y envíe la respuesta

            # Lee el estado y la posición del PLC
            response = plc.receive_response()

            if response:
                return jsonify(response), 200
            else:
                return jsonify({'error': 'No se pudo obtener el estado del PLC'}), 500
        except Exception as e:
            return jsonify({'error': f'Error al comunicarse con el PLC: {e}'}), 500

    else:
        return jsonify({'error': 'No se pudo conectar al PLC'}), 500

@app.route('/tires', methods=['GET', 'POST'])
def manage_tires():
    """
    Maneja las operaciones CRUD de llantas.
    """
    if request.method == 'GET':
        search_term = request.args.get('search')
        if search_term:
            tires = inventory_controller.find_tire(search_term)
            return jsonify(tires)
        else:
            tires = inventory_controller.get_all_tires()
            return jsonify(tires)

    elif request.method == 'POST':
        data = request.get_json()
        categoria_id = data.get('categoria_id')
        referencia = data.get('referencia')
        tamaño_rin = data.get('tamaño_rin')
        marca_id = data.get('marca_id')

        if categoria_id and referencia and tamaño_rin and marca_id:
            inventory_controller.add_tire(categoria_id, referencia, tamaño_rin, marca_id)
            return jsonify({'message': 'Llanta agregada exitosamente'}), 201
        else:
            return jsonify({'error': 'Faltan datos requeridos'}), 400

@app.route('/tires/<int:tire_id>', methods=['PUT', 'DELETE'])
def manage_tire(tire_id):
    """
    Maneja las operaciones de actualizar y eliminar una llanta específica.
    """
    if request.method == 'PUT':
        data = request.get_json()
        nuevos_datos = {key: value for key, value in data.items() if key in ['categoria_id', 'tamaño_rin', 'marca_id', 'ubicacion']}
        if nuevos_datos:
            inventory_controller.update_tire(tire_id, nuevos_datos)
            return jsonify({'message': 'Llanta actualizada exitosamente'}), 200
        else:
            return jsonify({'error': 'No se proporcionaron datos para actualizar'}), 400

    elif request.method == 'DELETE':
        inventory_controller.delete_tire(tire_id)
        return jsonify({'message': 'Llanta eliminada exitosamente'}), 200
    
@app.route('/brands', methods=['GET', 'POST'])
def manage_brands():
    """
    Maneja las operaciones CRUD de marcas.
    """
    if request.method == 'GET':
        search_term = request.args.get('search')
        if search_term:
            brands = brand_controller.find_brands(search_term)  # Asegúrate de implementar este método en BrandController
            return jsonify(brands)
        else:
            brands = brand_controller.get_all_brands()
            return jsonify(brands)
    elif request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre:
            brand_controller.add_brand(nombre)
            return jsonify({'message': 'Marca agregada exitosamente'}), 201
        else:
            return jsonify({'error': 'Falta el nombre de la marca'}), 400

@app.route('/brands/<int:brand_id>', methods=['PUT', 'DELETE'])
def manage_brand(brand_id):
    """
    Maneja las operaciones de actualizar y eliminar una marca específica.
    """
    if request.method == 'PUT':
        data = request.get_json()
        nuevo_nombre = data.get('nombre')
        if nuevo_nombre:
            brand_controller.update_brand(brand_id, nuevo_nombre)
            return jsonify({'message': 'Marca actualizada exitosamente'}), 200
        else:
            return jsonify({'error': 'Falta el nuevo nombre de la marca'}), 400
    elif request.method == 'DELETE':
        brand_controller.delete_brand(brand_id)
        return jsonify({'message': 'Marca eliminada exitosamente'}), 200

@app.route('/categories', methods=['GET', 'POST'])
def manage_categories():
    """
    Maneja las operaciones CRUD de categorías.
    """
    if request.method == 'GET':
        search_term = request.args.get('search')
        if search_term:
            categories = category_controller.find_categories(search_term)  # Asegúrate de implementar este método en CategoryController
            return jsonify(categories)
        else:
            categories = category_controller.get_all_categories()
            return jsonify(categories)
    elif request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre:
            category_controller.add_category(nombre)
            return jsonify({'message': 'Categoría agregada exitosamente'}), 201
        else:
            return jsonify({'error': 'Falta el nombre de la categoría'}), 400

@app.route('/categories/<int:category_id>', methods=['PUT', 'DELETE'])
def manage_category(category_id):
    """
    Maneja las operaciones de actualizar y eliminar una categoría específica.
    """
    if request.method == 'PUT':
        data = request.get_json()
        nuevo_nombre = data.get('nombre')
        if nuevo_nombre:
            category_controller.update_category(category_id, nuevo_nombre)
            return jsonify({'message': 'Categoría actualizada exitosamente'}), 200
        else:
            return jsonify({'error': 'Falta el nuevo nombre de la categoría'}), 400
    elif request.method == 'DELETE':
        category_controller.delete_category(category_id)
        return jsonify({'message': 'Categoría eliminada exitosamente'}), 200

@app.route('/move_to_tire', methods=['POST'])
def move_to_tire():
    """
    Mueve el carrusel al bucket donde se encuentra una llanta.
    """
    data = request.get_json()
    referencia = data.get('referencia')
    if referencia:
        inventory_controller.move_carousel_to_tire(referencia)
        return jsonify({'message': 'Comando de movimiento enviado'}), 200
    else:
        return jsonify({'error': 'Falta la referencia de la llanta'}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
