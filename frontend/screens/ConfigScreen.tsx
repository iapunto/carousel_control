import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Alert } from 'react-native';
import { Button, TextInput } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const ConfigScreen = () => {
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

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Configuración del PLC</Text>

      <TextInput
        placeholder="Dirección IP"
        value={plcIP}
        onChangeText={setPlcIP}
        keyboardType="numeric"
      />

      <TextInput
        placeholder="Puerto"
        value={plcPort}
        onChangeText={setPlcPort}
        keyboardType="numeric"
      />

      <Button title="Guardar Configuración" onPress={saveConfig} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
  },
});

export default ConfigScreen;