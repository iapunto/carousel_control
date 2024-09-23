import React from 'react';
import { View, StyleSheet, Text } from 'react-native';

interface PLCStatusProps {
  status: string;
}

const PLCStatus: React.FC<PLCStatusProps> = ({ status }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.statusTitle}>Estado del PLC:</Text>
      <Text>{status}</Text> 
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: 10,
  },
  statusTitle: {
    color: 'white',
    fontWeight: 'bold',
    marginBottom: 5,
  },
});

export default PLCStatus;