
import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Alert } from 'react-native';
import { Button, Input } from 'react-native-elements';
import axios from 'axios';
import { interpretarEstadoPLC } from '../utils/utils'; // Asegúrate de tener este archivo utils

const API_BASE_URL = 'http://127.0.0.1:5000'; // Reemplaza con la URL real de tu API

const HomeScreen = () => {
  const [status, setStatus] = useState('Estado del PLC: Desconocido');
  const [position, setPosition] = useState('Posición: Desconocida');
  const [bucketInput, setBucketInput] = useState('');

  useEffect(() => {
    // Actualiza el estado al inicio y cada 5 segundos
    fetchStatus();
    const intervalId = setInterval(fetchStatus, 5000);
    return () => clearInterval(intervalId);
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/status`);
      const estadosPLC = interpretarEstadoPLC(response.data.status_code);
      setStatus(`Estado del PLC:\n${Object.entries(estadosPLC).map(([key, value]) => `${key}: ${value}`).join('\n')}`);
      setPosition(`Posición: ${response.data.position}`);
    } catch (error) {
      console.error('Error al obtener el estado:', error);
      setStatus('Error al obtener el estado del PLC');
    }
  };

  const sendCommand = async (command: number, argument?: number) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/command`, {
        command,
        argument,
      });
      if (response.status === 200) {
        Alert.alert('Éxito', 'Comando enviado exitosamente');
        fetchStatus(); // Actualiza el estado después de enviar el comando
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

      <Input
        placeholder="Número de cangilón"
        onChangeText={setBucketInput}
        value={bucketInput}
        keyboardType="numeric"
      />
      <Button title="Mover" onPress={() => sendCommand(1, parseInt(bucketInput))} />

      {/* Agrega más botones y elementos de interfaz aquí */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  input: {
    marginBottom: 10,
  },
});

export default HomeScreen;