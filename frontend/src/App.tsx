import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Button, TextInput, Alert } from 'react-native';
import axios from 'axios';

const API_BASE_URL = 'http://127.0..1:5000'; // Reemplaza con la URL real de tu API

const App = () => {
  const [status, setStatus] = useState('Estado del PLC: Desconocido');
  const [position, setPosition] = useState('Posición: Desconocida');
  const [bucketInput, setBucketInput] = useState('');

  useEffect(() => {
    // Actualiza el estado al inicio y cada 5 segundos
    fetchStatus();
    const intervalId = setInterval(fetchStatus, 5000); 
    return () => clearInterval(intervalId); // Limpia el intervalo al desmontar el componente
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/status`);
      setStatus(`Estado del PLC: ${response.data.status_code}`);
      setPosition(`Posición: ${response.data.position}`);
    } catch (error) {
      console.error('Error al obtener el estado:', error);
      setStatus('Error al obtener el estado del PLC');
    }
  };

  const sendCommand = async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/command`, {
        command: 1, // Comando MUEVETE
        argument: bucketInput,
      });
      if (response.status === 200) {
        Alert.alert('Éxito', 'Comando enviado exitosamente');
        // Puedes actualizar el estado o realizar otras acciones aquí
      } else {
        Alert.alert('Error', 'Hubo un error al enviar el comando');
      }
    } catch (error) {
      console.error('Error al enviar el comando:', error);
      Alert.alert('Error', 'Hubo un error al enviar el comando');
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
        keyboardType="numeric" // Solo permite ingresar números
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