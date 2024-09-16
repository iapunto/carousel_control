from flask import Flask, jsonify, request
# O models.plc.PLC si estás usando el PLC real
from models.plc_simulator import PLCSimulator
from controllers.carousel_controller import CarouselController
from dotenv import load_dotenv
import os

load_dotenv()

plc_ip = os.getenv('PLC_IP')
plc_port = int(os.getenv('PLC_PORT'))

# O plc = PLC(plc_ip, plc_port) si usas el PLC real
plc = PLCSimulator(plc_ip, plc_port)
controller = CarouselController(plc)

app = Flask(__name__)


@app.route('/status', methods=['GET'])
def get_status():
    """Obtiene el estado y la posición actual del PLC."""
    if plc.connect():
        response = plc.send_command_and_receive_response("STATUS")
        plc.close()
        if response:
            return jsonify(response)
        else:
            return jsonify({'error': 'No se pudo obtener el estado del PLC'}), 500
    else:
        return jsonify({'error': 'No se pudo conectar al PLC'}), 500


@app.route('/command', methods=['POST'])
def send_command():
    """Envía un comando al PLC."""
    if plc.connect():
        data = request.get_json()
        command = data.get('command')
        argument = data.get('argument')

        if command:
            controller.send_command(command, argument)
            return jsonify({'message': 'Comando enviado exitosamente'}), 200
        else:
            return jsonify({'error': 'Comando no especificado'}), 400

        plc.close()
    else:
        return jsonify({'error': 'No se pudo conectar al PLC'}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
