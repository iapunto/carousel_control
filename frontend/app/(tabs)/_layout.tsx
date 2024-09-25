import React from "react";
import FontAwesome from '@expo/vector-icons/FontAwesome';
import { Tabs } from "expo-router";

export default function TabLayout() {
    return (
      <Tabs screenOptions={{ tabBarActiveTintColor: 'red' }}>
        <Tabs.Screen
          name="index"
          options={{
            title: 'Home',
            tabBarIcon: ({ color }) => <FontAwesome size={28} name="home" color={color} />
          }}
        />
        <Tabs.Screen
          name="settings"
          options={{
            title: 'Configuración',
            tabBarIcon: ({ color }) => <FontAwesome size={28} name="cogs" color={color} />
            }}
          />
      </Tabs>
    )
}