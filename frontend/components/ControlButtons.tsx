import React from 'react';
import { View, StyleSheet, Button } from 'react-native';

const ControlButtons: React.FC = () => {
  return (
    <View style={styles.container}>
      <Button title="Iniciar" onPress={() => {}} />
      <Button title="Home" onPress={() => {}} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'column',
    alignItems: 'flex-start',
    width: '40%',
    marginBottom: 20,
  },
});

export default ControlButtons;