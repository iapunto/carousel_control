import React from 'react';
import { StyleSheet, View, TextInput } from 'react-native';

interface BucketInputProps {
  value: string;
  onChangeText: (text: string) => void;
}

const BucketInput: React.FC<BucketInputProps> = ({ value, onChangeText }) => {
  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        value={value}
        onChangeText={onChangeText}
        keyboardType="numeric"
        placeholder="Número de cangilón"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: 20,
  },
  input: {
    height: 60,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 20,
    width: 200,
    textAlign: 'center',
    fontSize: 30,
  },
});

export default BucketInput;