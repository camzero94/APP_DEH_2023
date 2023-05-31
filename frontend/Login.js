import { StyleSheet, Text, View, TextInput, TouchableOpacity, ScrollView, TouchableWithoutFeedback, Keyboard } from 'react-native';
import {useState} from 'react'

import { Image } from 'react-native';
import { GRAY, GREEN, LIGHT_GREEN, LIGHT_RED, RED, WHITE } from './CONSTANTS';
import JWT from 'expo-jwt';
import { setToken } from './Utils';

export default function Login({navigation}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loginError, setLoginError] = useState(false);
  
  function login(navigation) {
    if(email.length == 0) return;
    if(password.length == 0) return;
  
    const form_data = new FormData()
    form_data.append("username", email)
    form_data.append("password", password)
  
    handleLoginToken(navigation, form_data);
  
  }

  async function handleLoginToken(navigation, form_data) {
    // Send data to the backend via POST
    const res = await fetch('https://b723-223-139-248-33.ngrok-free.app/api/token', {  // Enter your IP address here
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
        navigation.navigate("Home")
      } catch (e) {
        console.log('Error: ' + e)
      }
    }
    else {
      setLoginError(true)
    }
  }

  return (
    <ScrollView keyboardShouldPersistTaps='handled' style={{backgroundColor: LIGHT_GREEN}}>
      <View style={styles.container}>
        <Image source={require('./assets/logo.png')} style={[{ width: 150, height: 150}]} />

        {
          loginError ?  
          <View style={styles.inputViewError}>
              <TextInput
                  style={styles.TextInput}
                  placeholder="Email"
                  onChangeText={(email) => setEmail(email)}
              />
          </View>
          :
          <View style={styles.inputView}>
              <TextInput
                  style={styles.TextInput}
                  placeholder="Email"
                  onChangeText={(email) => setEmail(email)}
              />
          </View>
        }
        
        {
          loginError ?
          <View style={styles.inputViewError}>
            <TextInput
                style={styles.TextInput}
                placeholder="Password"
                secureTextEntry={true}
                onChangeText={(password) => setPassword(password)}
              />
          </View> 
          :
          <View style={styles.inputView}>
            <TextInput
                style={styles.TextInput}
                placeholder="Password"
                secureTextEntry={true}
                onChangeText={(password) => setPassword(password)}
              />
          </View>
        }
        
        <TouchableOpacity style={styles.loginBtn} onPress={() => {
            login(navigation)
          }}>
          <Text style={styles.text}>Login</Text>
        </TouchableOpacity>

        <TouchableOpacity onPress={() => {
          navigation.navigate('Register');
        }}>
          <Text style={styles.signup_button}><Text style={{color: "#000", fontWeight: "black"}}>Don't Have an Account? </Text>Sign Up</Text> 
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
    paddingTop: 125,
    height: '100%'
  },
  inputView: {
    backgroundColor: WHITE,
    borderRadius: 30,
    width: "75%",
    height: 45,
    marginBottom: 20,
    alignItems: "center",
  },
  inputViewError: {
    backgroundColor: LIGHT_RED,
    borderColor: RED,
    borderWidth: 1,
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
  signup_button: {
    height: 30,
    marginTop: 40,
    marginBottom: 10,
    color: GREEN,
    fontWeight: 'bold'
  },
  text: {
    color: WHITE
  },
  loginBtn: { 
    width: "80%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
    backgroundColor: GREEN,
  }

});
