import React, { useState } from 'react';
import { StyleSheet, View, Text, Button, TextInput } from 'react-native';
import axios from 'axios';

const App = () => {
  const [status, setStatus] = useState('Estado del PLC: Desconocido');
  const [position, setPosition] = useState('Posición: Desconocida');
  const [bucketInput, setBucketInput] = useState('');

  const fetchStatus = async () => {
    try {
      const response = await axios.get('http://127.0.0.1/status');
      setStatus(`Estado del PLC: ${response.data.status_code}`);
      setPosition(`Posición: ${response.data.position}`);
    } catch (error) {
      console.error('Error al obtener el estado:', error);
      setStatus('Error al obtener el estado del PLC');
    }
  };

  const sendCommand = async () => {
    try {
      await axios.post('http://127.0.0.1/command', {
        command: 1, // Comando MUEVETE
        argument: bucketInput,
      });
      // Puedes actualizar el estado o mostrar un mensaje de éxito aquí
    } catch (error) {
      console.error('Error al enviar el comando:', error);
      // Puedes mostrar un mensaje de error aquí
    }
  };

  return (
    <View style={styles.container}>
      <Button title="Actualizar Estado" onPress={fetchStatus} />
      <Text>{status}</Text>
      <Text>{position}</Text>

      <TextInput
        style={styles.input}
        placeholder="Número de cangilón"
        onChangeText={setBucketInput}
        value={bucketInput}
      />
      <Button title="Mover" onPress={sendCommand} />

      {/* Agrega más botones y elementos de interfaz aquí */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});

export default App;