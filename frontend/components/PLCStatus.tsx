import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface PLCStatusProps {
  status: string;
}

const PLCStatus: React.FC<PLCStatusProps> = ({ status }) => {
  return (
    <View style={styles.statusContainer}>
      <Text style={styles.statusTitle}>Estado del PLC:</Text>
      <Text className="text-white">{status}</Text> 
    </View>
  );
};

const styles = StyleSheet.create({
  statusContainer: {
    marginBottom: 10,
  },
  statusTitle: {
    color: 'white',
    fontWeight: 'bold',
    marginBottom: 5,
  },
});

export default PLCStatus;