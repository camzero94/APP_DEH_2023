// Sign up page

import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button } from 'react-native';
import {useState, useRef} from 'react'
import JWT from 'expo-jwt';

import { Image } from 'react-native';
import { BLUE, LIGHT_BLUE } from './CONSTANTS';

import { setToken } from './Utils';

export default function Login({navigation}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  return (
    <View style={styles.container}>
      <Image source={require('./assets/logo.png')} style={[{ width: 150, height: 150}]} />

      <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Email"
            placeholderTextColor="#fff"
            onChangeText={(email) => setEmail(email)}
        />
      </View>

      <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Password"
            placeholderTextColor="#fff"
            secureTextEntry={true}
            onChangeText={(password) => setPassword(password)}
          />
      </View>

      <TouchableOpacity style={styles.loginBtn} onPress={register(navigation, email, password)}>
        <Text style={styles.text}>Sign Up</Text>
      </TouchableOpacity>
    </View>
  );
}

function register(navigation, email, password) {
  if(email.length == 0) return;
  if(password.length == 0) return;

  const form_data = new FormData()
  form_data.append("username", email)
  form_data.append("password", password)

  handleToken(navigation, form_data);

  
}

async function handleToken(navigation, form_data) {
    
  // Send data to the backend via POST
  const res = await fetch('https://f6a7-140-116-1-143.ngrok-free.app/api/signup', {  // Enter your IP address here

    method: 'POST', 
    mode: 'cors', 
    body: form_data // body data type must match "Content-Type" header
  })

  const data = await res.json()

  if('access_token' in data) {
    const decodeToken = JWT.decode(data['access_token'], 'SECRET')
    try {
      setToken('token', data['access_token'])
      setToken('permissions', decodeToken.permissions)
      setToken('id', decodeToken.id.toString())
      navigation.navigate("Login")
    } catch (e) {
      console.log('Error: ' + e)
    }
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'top',
    paddingTop: 125,
  },
  inputView: {
    backgroundColor: LIGHT_BLUE,
    borderRadius: 30,
    width: "75%",
    height: 45,
    marginBottom: 20,
    alignItems: "center",
  },
  TextInput: {
    color: "#fff",
    placeholderTextColor: "white",
    height: 50,
    flex: 1,
    padding: 10,
    width: "75%",
    textAlign: "center"
  },
  signup_button: {
    height: 30,
    marginTop: 40,
    marginBottom: 10,
  },
  forgot_button: {
    height: 30,
    marginBottom: 0,
  },
  text: {
    color: "white"
  },
  loginBtn: { 
    width: "80%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
    backgroundColor: BLUE,
  }

});
