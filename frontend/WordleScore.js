import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image, ScrollView } from 'react-native';
import {useState, useRef} from 'react'
import { BLUE, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, LIGHT_YELLOW, RED, WHITE, YELLOW } from './CONSTANTS';

export default function WordleScore({navigation, route}) {
  const finalScore = route.params.score
  return (
      <View style={styles.container}>
        <Text style={{fontSize: 50}}>Score</Text>
        <Text style={{fontSize: 50, marginTop: 10}}>{finalScore}</Text>
        {
          finalScore ? 
          <Image source={require('./assets/trophy.png')} style={[{ width: 150, height: 150, marginTop: 25,}]}  />
          :
          <Image source={require('./assets/cry.png')} style={[{ width: 150, height: 150, marginTop: 25,}]}  />
        }
        

        <TouchableOpacity style={styles.btn} onPress={() => {
          navigation.navigate('Home')
        }}>
        <Text style={styles.btnText}>Back</Text>
      </TouchableOpacity>
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: LIGHT_GREEN,
    alignItems: 'center',
    justifyContent: 'top',
    paddingTop: 100,
    paddingBottom: 100,
  },
  btn: { 
    width: "55%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 50,
    backgroundColor: GREEN,
  },
  btnText: {
    color: "white",
    fontWeight: "bold", 
    fontSize: 24
  }
});
