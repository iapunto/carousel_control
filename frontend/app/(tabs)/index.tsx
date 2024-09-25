import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Alert } from 'react-native';
import axios from 'axios';
import { interpretarEstadoPLC } from '../../utils/utils';

// Importa los componentes
import StatusIndicators from '../../components/StatusIndicators';
import CarouselControls from '../../components/CarouselControls';
import PLCStatus from '../../components/PLCStatus';

const API_BASE_URL = 'http://localhost:5000'; // Reemplaza con la URL real de tu API

const HomeScreen = () => {
  const [status, setStatus] = useState('Estado del PLC: Desconocido');
  const [position, setPosition] = useState('Posición: Desconocida');
  const [bucketInput, setBucketNumber] = useState('0');
  const [isConnected, setIsConnected] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  useEffect(() => {
    // Actualiza el estado al inicio y cada 5 segundos
    fetchStatus();
    // const intervalId = setInterval(fetchStatus, 5000);
    return () => {
      // clearInterval(intervalId); // Limpia el intervalo al desmontar el componente
      // controller.close_connection(); // Cierra la conexión con el PLC
      fetchStatus();
    };
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/v1/status`);
      console.log('Respuesta completa de la API:', response); // Imprime la respuesta completa
      console.log('Datos de la respuesta:', response.data);  // Imprime solo los datos de la respuesta
      
      // Asegúrate de que la respuesta tenga la estructura esperada
      if (response.data && response.data.status_code !== undefined) {
        const estadosPLC = interpretarEstadoPLC(response.data.status_code);
        setStatus(`Estado del PLC:\n${Object.entries(estadosPLC).map(([key, value]) => `${key}: ${value}`).join('\n')}`);
        setPosition(`Posición: ${response.data.position}`);
        setIsConnected(true);
        setShowAlert(estadosPLC['ALARMA'] === 'Alarma activa');
      } else {
        console.error('Respuesta inesperada del servidor:', response.data);
        setStatus('Error al obtener el estado del PLC');
        setIsConnected(false);
      }
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error('Error de Axios:', error.message);
        if (error.response) {
          // La solicitud se hizo y el servidor respondió con un código de estado 
          // que está fuera del rango de 2xx
          console.error('Datos de la respuesta de error:', error.response.data);
          console.error('Estado de la respuesta de error:', error.response.status);
          console.error('Encabezados de la respuesta de error:', error.response.headers);
        } else if (error.request) {
          // La solicitud se hizo pero no se recibió respuesta
          // `error.request` es una instancia de XMLHttpRequest en el navegador y un objeto ClientRequest en node.js
          console.error('Solicitud realizada pero no se recibió respuesta:', error.request);
        } else {
          // Algo sucedió al configurar la solicitud que desencadenó un error
          console.error('Error al configurar la solicitud:', error.config);
        }
      } else {
        // Si el error no es de Axios, simplemente imprímelo en la consola
        console.error('Error al obtener el estado:', error);
      }
      setStatus('Error al obtener el estado del PLC');
      setIsConnected(false);
    }
  };

  const sendCommand = async (command: number, argument?: number) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/v1/command`, {
        command,
        argument,
      });

      console.log('Respuesta al enviar comando:', response); // Imprime la respuesta completa


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

  const incrementBucket = () => {
    const newBucket = Math.min(parseInt(bucketInput) + 1, 10); 
    setBucketNumber(newBucket.toString());
  };

  const decrementBucket = () => {
    const newBucket = Math.max(parseInt(bucketInput) - 1, 0); 
    setBucketNumber(newBucket.toString());
  };

  return (
    <View style={styles.container}>
      <StatusIndicators isConnected={isConnected} showAlert={showAlert} />

      <CarouselControls 
        bucketNumber={bucketInput} 
        setBucketNumber={setBucketNumber} 
        onIniciar={() => sendCommand(1, parseInt(bucketInput))} 
        onHome={() => sendCommand(4)} 
      />

      <PLCStatus status={status} />
      {/* <Text className="text-white">Posición actual del carrusel: {position}</Text> */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6c6c6c',
    alignItems: 'center',
    padding: 20,
  },
});

export default HomeScreen;