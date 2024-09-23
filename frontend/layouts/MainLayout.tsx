import React from 'react';
import { StyleSheet, View, useWindowDimensions } from 'react-native';

interface MainLayoutProps {
  children: React.ReactNode;
}

const MainLayout: React.FC<MainLayoutProps> = ({ children }) => {
  const { width } = useWindowDimensions();
  const isSmallScreen = width < 600;

  return (
    <View style={[styles.container, isSmallScreen && styles.columnLayout]}>
      {children}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'row', // Disposición horizontal por defecto
    justifyContent: 'space-around',
    alignItems: 'center',
  },
  columnLayout: {
    flexDirection: 'column', // Disposición vertical en pantallas pequeñas
  },
});

export default MainLayout;