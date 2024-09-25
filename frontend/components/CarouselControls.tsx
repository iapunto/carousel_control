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
    <View className="flex flex-col w-full items-center">

      <View className="flex flex-row items-center mb-6">
        <TextInput
          className="h-40 w-40 border border-gray-400 px-4 w-48 text-center text-8xl mr-4"
          value={bucketNumber}
          onChangeText={setBucketNumber}
          keyboardType="numeric"
          placeholder="0"
          maxLength={1} 
        />

        <View className="flex flex-col mt-4">
          <TouchableOpacity className="bg-red-500 w-20 h-20 rounded-lg justify-center items-center mb-2" onPress={incrementBucket}>
            <Icon name="caret-up" size={24} color="white" />
          </TouchableOpacity>
          <TouchableOpacity className="bg-red-500 w-20 h-20 rounded-lg justify-center items-center" onPress={decrementBucket}>
            <Icon name="caret-down" size={24} color="white" />
          </TouchableOpacity>
        </View>
      </View>

      <View className="flex flex-row items-center mb-6">
        <TouchableOpacity className="bg-red-700 py-3 px-9 rounded-md mb-2" onPress={onIniciar}>
          <Text className="text-white font-bold">Iniciar</Text>
        </TouchableOpacity>
        <TouchableOpacity className="bg-red-700 py-3 px-9 rounded-md mb-2 ml-2" onPress={onHome}>
          <Text className="text-white font-bold">Home</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default CarouselControls;