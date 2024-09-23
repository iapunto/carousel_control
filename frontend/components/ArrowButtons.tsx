import React from 'react';
import { View, StyleSheet, TouchableOpacity, Text } from 'react-native';

interface ArrowButtonsProps {
  onIncrement: () => void;
  onDecrement: () => void;
}

const ArrowButtons: React.FC<ArrowButtonsProps> = ({ onIncrement, onDecrement }) => {
  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.arrowButton} onPress={onIncrement}>
        <Text style={styles.arrowButtonText}>▲</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.arrowButton} onPress={onDecrement}>
        <Text style={styles.arrowButtonText}>▼</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
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
});

export default ArrowButtons;