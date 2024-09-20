import React, { useState } from 'react';
import { StyleSheet, View, Text, Button, TextInput, TouchableOpacity, Image } from 'react-native';

const HomeScreen = () => {
  const [bucketInput, setBucketInput] = useState('0');

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
    </View>
  );
};

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
    backgroundColor: 'blue',
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