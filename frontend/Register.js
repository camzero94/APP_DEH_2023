// Sign up page

import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button } from 'react-native';
import {useState, useRef} from 'react'
import JWT from 'expo-jwt';

import { Image } from 'react-native';
import { BLUE, LIGHT_GREEN, WHITE, GRAY, GREEN } from './CONSTANTS';

import { setToken } from './Utils';

export default function Login({navigation}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

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
    const res = await fetch('https://b723-223-139-248-33.ngrok-free.app/api/signup', {  // Enter your IP address here
  
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
  

  return (
    <View style={styles.container}>
      <Image source={require('./assets/logo.png')} style={[{ width: 150, height: 150}]} />

      <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Email"
            onChangeText={(email) => setEmail(email)}
        />
      </View>

      <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Password"
            secureTextEntry={true}
            onChangeText={(password) => setPassword(password)}
          />
      </View>

      <TouchableOpacity style={styles.loginBtn} onPress={register(navigation, email, password)}>
        <Text style={styles.text}>Sign Up</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => {
          navigation.navigate('Login');
        }}>
          <Text style={styles.signup_button}><Text style={{color: "#000", fontWeight: 'black'}}>Already Have an Account? </Text>Login</Text> 
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
    paddingTop: 125,
  },
  inputView: {
    backgroundColor: WHITE,
    borderRadius: 30,
    width: "75%",
    height: 45,
    marginBottom: 20,
    alignItems: "center",
  },
  TextInput: {
    color: GRAY,
    height: 50,
    flex: 1,
    padding: 10,
    width: "75%",
    textAlign: "center"
  },
  text: {
    color: "white"
  },
  signup_button: {
    height: 30,
    marginTop: 40,
    marginBottom: 10,
    color: BLUE,
    fontWeight: 'bold'
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
