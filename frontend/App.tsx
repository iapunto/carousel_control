<<<<<<< HEAD
import React, { useState } from 'react';
import { StyleSheet, View, Text, Button, TextInput, TouchableHighlight, TouchableOpacity, Image } from 'react-native';
=======
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
>>>>>>> ce4ca6b9197f35f72cfd01208a4b3bf040866bd2

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
<<<<<<< HEAD
    const newBucket = Math.max(parseInt(bucketInput) - 1, 1);
=======
    const newBucket = Math.max(parseInt(bucketInput) - 1, 0);
>>>>>>> ce4ca6b9197f35f72cfd01208a4b3bf040866bd2
    setBucketInput(newBucket.toString());
  };

  return (
    <View style={styles.container}>
<<<<<<< HEAD
      {/* Iconos de conexión y alerta */}
      <View style={styles.topIcons}>
        <Image source={require('./assets/connect_icon.png')} style={styles.icon} /> 
        <Image source={require('./assets/alert_icon.png')} style={styles.icon} />
      </View>
      <View style={styles.container}>
        { /* logo de la empresa */ }
        <Image
            source={require('./assets/logo.png')} // Reemplaza con la ruta a tu logo
            style={styles.logo}
        />
      </View>

      {/* Fila principal con tres columnas */}
      <View style={styles.mainRow}>
        {/* Columna 1: Botones Iniciar y Home */}
        <View style={styles.column}>
          <Button title="Iniciar" onPress={() => {}} />
          <Button title="Home" onPress={() => {}} />
        </View>

        {/* Columna 2: Input de número de bucket y botones de flecha */}
        <View style={styles.column}>
          <TextInput
            style={styles.bucketInput}
            value={bucketInput}
            onChangeText={setBucketInput}
            keyboardType="numeric"
            placeholder="Número de cangilón"
          />

          <View style={styles.arrowButtons}>
            <TouchableOpacity style={styles.arrowButton} onPress={incrementBucket}>
              <Text style={styles.arrowButtonText}>▲</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.arrowButton} onPress={decrementBucket}>
              <Text style={styles.arrowButtonText}>▼</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Columna 3: (vacía por ahora) */}
        <View style={styles.column} />
      </View>

      {/* Estado del PLC */}
      <View style={styles.statusContainer}>
        <Text style={styles.statusTitle}>Estado del PLC:</Text>
        {/* Aquí puedes mostrar los estados del PLC */}
      </View>
=======
      <StatusIndicators isConnected={isConnected} showAlert={showAlert} />
        <MainLayout> {/* Utiliza el componente MainLayout para la maquetación principal */}
          <ControlButtons />
          <BucketInput value={bucketInput} onChangeText={setBucketInput} />
          <ArrowButtons onIncrement={incrementBucket} onDecrement={decrementBucket} />
          {/* Puedes agregar una tercera columna aquí si es necesario */}
        </MainLayout>
    
        <PLCStatus status={status} />
        <Text>Posición actual del carrusel: {position}</Text>
>>>>>>> ce4ca6b9197f35f72cfd01208a4b3bf040866bd2
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

<<<<<<< HEAD
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  logo: {
    height: 150,    // Altura fija de 50px
    resizeMode: 'contain', // Escala la imagen para que quepa dentro del contenedor sin deformarla
    position: 'absolute', // Posicionamiento absoluto
    top: 20,        // Margen superior de 20px
  },
  topIcons: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    width: '60%',
    marginBottom: 30,
  },
  icon: {
    width: 30,
    height: 30,
    marginRight: 10,
  },
  mainRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
    marginBottom: 20,
    alignContent: 'center',
    alignItems: 'center',
  },
  column: {
    flex: 1,
    alignItems: 'center',
  },
  bucketInputContainer: {
    marginBottom: 20,
  },
  bucketInput: {
    height: 200,
    width: 200,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 20,
    textAlign: 'center',
    fontSize: 100,
  },
  arrowButtons: {
    flexDirection: 'column',
  },
  arrowButton: {
    backgroundColor: 'red',
    width: 80,
    height: 80,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
  },
  arrowButtonText: {
    color: 'white',
    fontSize: 30,
  },
  statusContainer: {
    marginBottom: 10,
  },
  statusTitle: {
    color: 'white',
    fontWeight: 'bold',
    marginBottom: 5,
  },
});

export default HomeScreen;
=======
export default App;
>>>>>>> ce4ca6b9197f35f72cfd01208a4b3bf040866bd2
