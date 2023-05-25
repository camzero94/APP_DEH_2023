import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image } from 'react-native';
import {useState, useRef} from 'react'
import { BLUE, LIGHT_BLUE, LIGHT_YELLOW, RED, YELLOW } from './CONSTANTS';

export default function Home({navigation}) {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/logo.png')} style={[{ width: 150, height: 150}]} />


      <TouchableOpacity style={styles.placeContainerYELLOW} onPress={() => {
          navigation.navigate('POI', {id: 3})
        }}>
        <Text style={styles.placeContainerText}>Hello</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.placeContainerYELLOW} onPress={() => {
          navigation.navigate('POI', {id: 2})
        }}>
        <Text style={styles.placeContainerText}>Hello</Text>
      </TouchableOpacity>

      {/* <View style={styles.placeContainer} backgroundColor={BLUE}>
        <Text style={styles.placeContainerText}>Hello</Text>
      </View>

      <View style={styles.placeContainer} backgroundColor={RED}>
        <Text style={styles.placeContainerText}>Hello</Text>
      </View> */}
    </View>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'top',
    paddingTop: 50
  },

  placeContainerYELLOW: {
    backgroundColor: YELLOW,
    borderRadius: 10,
    width: "90%",
    height: 80,
    marginTop: 20,
    alignItems: "left",
    justifyContent: "center"
  },

  placeContainerText: {
    color: "white",
    fontSize: 50,
    fontWeight: "bold"
  }
});
