import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image, ScrollView } from 'react-native';
import {useState, useRef} from 'react'
import { BLUE, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, LIGHT_YELLOW, RED, WHITE, YELLOW } from './CONSTANTS';

export default function Home({navigation}) {
  return (
    <ScrollView style={{backgroundColor: LIGHT_GREEN}} showsVerticalScrollIndicator={false}>
      <View style={styles.container}>

        <Image source={require('./assets/logo.png')} style={[{ width: 150, height: 150}]}  />

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 11})
          }}>
          <View style={styles.barYELLOW} />
          <View>
            <Text style={styles.placeContainerText}>Monument de Blas de Lezo</Text>
          </View>
        </TouchableOpacity>

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 12})
          }}>
          <View style={styles.barYELLOW} />
          <View>
            <Text style={styles.placeContainerText}>Las Botas Viejas</Text>
          </View>
        </TouchableOpacity>

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 13})
          }}>
          <View style={styles.barBLUE} />
          <Text style={styles.placeContainerText}>Club de pesca de Cartagena</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 14})
          }}>
          <View style={styles.barBLUE} />
          <Text style={styles.placeContainerText}>Centro Histórico de Cartagena</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 15})
          }}>
          <View style={styles.barRED} />
          <Text style={styles.placeContainerText}>Castillo de San Felipe de Barajas</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.placeContainer} onPress={() => {
            navigation.navigate('POI', {id: 16})
          }}>
          <View style={styles.barRED} />
          <Text style={styles.placeContainerText}>Monumento a India Catalina</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: LIGHT_GREEN,
    alignItems: 'center',
    justifyContent: 'top',
    paddingTop: 50,
    paddingBottom: 100,
  },

  placeContainer: {
    backgroundColor: WHITE,
    borderRadius: 25,
    width: "90%",
    height: 80,
    marginTop: 10,
    marginBottom: 10,
    alignItems: "center",
    flexDirection: "row",
    shadowColor: 'rgba(0,0,0, .4)', // IOS
    shadowOffset: { height: 1, width: 1 }, // IOS
    shadowOpacity: 1, // IOS
    shadowRadius: 1, //IOS
    elevation: 2, // Android
  },

  placeContainerText: {
    color: BLUE,
    fontSize: 18,
    fontWeight: "bold",
    
  },
  
  barYELLOW: {
    backgroundColor: LIGHT_YELLOW,
    width: 7.5,
    height: 50,
    marginLeft: 15,
    marginRight: 15,
  },

  barBLUE: {
    backgroundColor: LIGHT_BLUE,
    width: 7.5,
    height: 50,
    marginLeft: 15,
    marginRight: 15,
  },

  barRED: {
    backgroundColor: LIGHT_RED,
    width: 7.5,
    height: 50,
    marginLeft: 15,
    marginRight: 15,
  },
});
