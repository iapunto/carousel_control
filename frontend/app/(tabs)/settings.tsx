import React, { useState, useEffect } from 'react';
import { Text, View, StyleSheet, TextInput, Button, Alert} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';


const Settings = () => {
  const [plcIP, setPlcIP] = useState('');
  const [plcPort, setPlcPort] = useState('');

  useEffect(() => {
    // Cargar la configuración guardada al montar el componente
    loadConfig();
  }, []);

  const loadConfig = async () => {
    try {
      const storedIP = await AsyncStorage.getItem('plcIP');
      const storedPort = await AsyncStorage.getItem('plcPort');
      if (storedIP) {
        setPlcIP(storedIP);
      }
      if (storedPort) {
        setPlcPort(storedPort);
      }
    } catch (error) {
      console.error('Error al cargar la configuración:', error);
    }
  };

  const saveConfig = async () => {
    try {
      await AsyncStorage.setItem('plcIP', plcIP);
      await AsyncStorage.setItem('plcPort', plcPort);
      Alert.alert('Éxito', 'Configuración guardada');
    } catch (error) {
      console.error('Error al guardar la configuración:', error);
      Alert.alert('Error', 'No se pudo guardar la configuración');
    }
  };

  const clearConfig = () => {
    setPlcIP('');
    setPlcPort('');
  };

  return (
    <View className="flex-1 p-4 bg-gray-800">
      <Text className="text-white text-2xl font-bold mb-4">Configuración del PLC</Text>

      <TextInput
        label="Dirección IP"
        placeholder="Ingresa la dirección IP del PLC"
        value={plcIP}
        onChangeText={setPlcIP}
        keyboardType="numeric"
        TextInputContainerStyle={styles.inputContainer}
        inputStyle={styles.input}
        labelStyle={styles.label}
      />

      <TextInput
        placeholder="Ingresa el puerto del PLC"
        value={plcPort}
        onChangeText={setPlcPort}
        keyboardType="numeric"
        inputContainerStyle={styles.inputContainer}
        inputStyle={styles.input}
        labelStyle={styles.label}
      />

      <View className="flex flex-row justify-around mt-4">
        <Button title="Guardar Configuración" onPress={saveConfig} 
          buttonStyle={styles.saveButton}
          titleStyle={styles.buttonText}
        />
        <Button title="Limpiar" onPress={clearConfig} 
          buttonStyle={styles.clearButton}
          titleStyle={styles.buttonText}
        />
      </View>
    </View>
  )
}
const styles = StyleSheet.create({
  inputContainer: {
    borderBottomWidth: 1,
    borderBottomColor: 'white',
    marginBottom: 20,
  },
  input: {
    color: 'white',
  },
  label: {
    color: 'white',
    marginBottom: 5,
  },
  saveButton: {
    backgroundColor: 'blue',
    borderRadius: 5,
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  clearButton: {
    backgroundColor: 'red',
    borderRadius: 5,
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  }
});

export default Settings;