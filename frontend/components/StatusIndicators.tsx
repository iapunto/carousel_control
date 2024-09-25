import React, { useState, useEffect } from 'react';
import { View, Image, StyleSheet } from 'react-native';
import Icon from '@expo/vector-icons/FontAwesome';

const StatusIndicators: React.FC = () => {
  const [isConnected, setIsConnected] = useState(true); // Estado inicial: conectado
  const [showAlert, setShowAlert] = useState(true);   // Estado inicial: sin alerta

  useEffect(() => {
    // Simula cambios de estado cada cierto tiempo (puedes ajustar el intervalo)
    const intervalId = setInterval(() => {
      setIsConnected(Math.random() < 0.8); // 80% de probabilidad de estar conectado
      setShowAlert(Math.random() < 0.2);   // 20% de probabilidad de mostrar una alerta
    }, 5000);

    return () => clearInterval(intervalId); // Limpia el intervalo al desmontar el componente
  }, []);

  return (
    <View className="flex flex-row top-0 justify-between items-center w-full p-4 bg-red-800"> 
      <Icon
        name={showAlert ? "exclamation-triangle" : 'check-circle'}
        size={24}
        color={showAlert ? 'red' : 'green'}
        style={styles.icon}
      />

      <View className="text-center">
        <Image 
          source={require('../assets/logo-w.png')}
          style={{ width: 250, height: 100, resizeMode: 'contain' }} />
      </View>
      <Icon 
        name={'server'} 
        size={24} 
        color={isConnected ? 'green' : 'red'} 
        style={styles.icon}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  icon: {
    alignSelf: 'flex-start', // Alinea los iconos a la izquierda/derecha según su posición
  },
});

export default StatusIndicators;