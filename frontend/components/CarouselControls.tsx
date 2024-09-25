import React from 'react';
import { View, Button, TextInput, TouchableOpacity, Text } from 'react-native';
import Icon from '@expo/vector-icons/FontAwesome';

interface CarouselControlsProps {
  bucketNumber: string;
  setBucketNumber: (text: string) => void;
  onIniciar: () => void;
  onHome: () => void;
}

const CarouselControls: React.FC<CarouselControlsProps> = ({ bucketNumber, setBucketNumber, onIniciar, onHome }) => {

  const incrementBucket = () => {
    const newBucket = Math.min(parseInt(bucketNumber) + 1, 9); 
    setBucketNumber(newBucket.toString());
  };

  const decrementBucket = () => {
    const newBucket = Math.max(parseInt(bucketNumber) - 1, 0); 
    setBucketNumber(newBucket.toString());
  };

  return (
    <View className="flex flex-row justify-around w-full mb-6">
      <View className="flex flex-col items-center">
        <Button title="Iniciar" onPress={onIniciar} />
        <Button title="Home" onPress={onHome} />
      </View>

      <View className="flex flex-col items-center">
        <TextInput
          className="h-16 border border-gray-400 px-4 w-48 text-center text-3xl mr-4"
          value={bucketNumber}
          onChangeText={setBucketNumber}
          keyboardType="numeric"
          placeholder="0"
          maxLength={1} 
        />

        <View className="flex flex-col mt-4">
          <TouchableOpacity className="bg-blue-500 w-20 h-20 rounded-lg justify-center items-center" onPress={incrementBucket}>
            <Icon name="caret-up" size={24} color="white" />
          </TouchableOpacity>
          <TouchableOpacity className="bg-blue-500 w-20 h-20 rounded-lg justify-center items-center mt-2" onPress={decrementBucket}>
            <Icon name="caret-down" size={24} color="white" />
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
};

export default CarouselControls;