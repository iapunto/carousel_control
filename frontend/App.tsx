import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import axios from 'axios';
import { interpretarEstadoPLC } from './utils/utils';

// Importa los componentes
import ArrowButtons from './components/ArrowButtons';
import BucketInput from './components/BucketInput';
import ControlButtons from './components/ControlButtons';
import StatusIndicators from './components/StatusIndicators';
import PLCStatus from './components/PLCStatus';
import MainLayout from './layouts/MainLayout';
import ConfigScreen from './screens/ConfigScreen';

const API_BASE_URL = 'http://127.0.0.1:5000'; // Reemplaza con la URL real de tu API
const Tab = createBottomTabNavigator();

const HomeScreen = () => {
  const [status, setStatus] = useState('Estado del PLC: Desconocido');
  const [position, setPosition] = useState('Posición: Desconocida');
  const [bucketInput, setBucketInput] = useState('0');
  const [isConnected, setIsConnected] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

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
      setIsConnected(true);
      setShowAlert(estadosPLC['ALARMA'] === 'Alarma activa');
    } catch (error) {
      console.error('Error al obtener el estado:', error);
      setStatus('Error al obtener el estado del PLC');
      setIsConnected(false);
    }
  };

  const sendCommand = async (command: number, argument?: number) => {
    // ... (lógica para enviar comandos a la API)
  };

  const incrementBucket = () => {
    const newBucket = Math.min(parseInt(bucketInput) + 1, 10);
    setBucketInput(newBucket.toString());
  };

  const decrementBucket = () => {
    const newBucket = Math.max(parseInt(bucketInput) - 1, 0);
    setBucketInput(newBucket.toString());
  };

  return (
    <View style={styles.container}>
      <StatusIndicators isConnected={isConnected} showAlert={showAlert} />
        <MainLayout> {/* Utiliza el componente MainLayout para la maquetación principal */}
          <ControlButtons />
          <BucketInput value={bucketInput} onChangeText={setBucketInput} />
          <ArrowButtons onIncrement={incrementBucket} onDecrement={decrementBucket} />
          {/* Puedes agregar una tercera columna aquí si es necesario */}
        </MainLayout>
    
        <PLCStatus status={status} />
        <Text>Posición actual del carrusel: {position}</Text>
    </View>
  );


// ... (estilos)

const App = () => {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Config" component={ConfigScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
};

export default App;