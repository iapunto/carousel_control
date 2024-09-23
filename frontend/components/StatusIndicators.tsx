import React from 'react';
import { View, StyleSheet, Image } from 'react-native';

interface StatusIndicatorsProps {
  isConnected: boolean;
  showAlert: boolean;
}

const StatusIndicators: React.FC<StatusIndicatorsProps> = ({ isConnected, showAlert }) => {
  return (
    <View style={styles.container}>
      <Image source={require('../assets/connect_icon.png')} style={[styles.icon, !isConnected && styles.disconnected]} /> 
      {showAlert && <Image source={require('../assets/alert_icon.png')} style={styles.icon} />}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    width: '80%',
    marginBottom: 30,
  },
  icon: {
    width: 30,
    height: 30,
    marginRight: 10,
  },
  disconnected: {
    tintColor: 'red', // Cambia el color del icono de conexión si está desconectado
  },
});

export default StatusIndicators;