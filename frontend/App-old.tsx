import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button, TouchableHighlight } from 'react-native';

export default function App() {
  return (
    <View
        style= {[
          styles.container,
          {
            flexDirection: 'column'
          },
        ]}>
      <View style={ styles.container }>
        <StatusBar style='light' />
        <TouchableHighlight
            underlayColor={"#000"}
            onPress={() => alert('hola')}
            style={{ width: 200, height: 30, backgroundColor: '#ff0000', borderRadius: 10, justifyContent: 'center', alignItems: 'center' }}
          >
          <Text style={{ color: 'white' }}>Pulsa aquí</Text>
        </TouchableHighlight>
        <View style={{ flex: 2 }}>
          <Text style= {{ color: 'white' }}>Estamos dise&ntilde;ando</Text>
        </View>
      </View>
    </View>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#3c3c3c',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
