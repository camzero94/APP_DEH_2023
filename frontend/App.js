import * as React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import { TouchableWithoutFeedback, Keyboard, ScrollView } from 'react-native';

import Login from './Login'
import Home from './Home'
import Register from './Register'
import Wordle from './Wordle'
import POI from './POI'
import WordleScore from './WordleScore';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
                                  
      <NavigationContainer>
        <Stack.Navigator initialRouteName='Login'> 
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen name="Home" component={Home} />
          <Stack.Screen name="Register" component={Register} />
          <Stack.Screen name="Wordle" component={Wordle} />
          <Stack.Screen name="WordleScore" component={WordleScore} />
          <Stack.Screen name="POI" component={POI} />
        </Stack.Navigator>
      </NavigationContainer>
    
    </TouchableWithoutFeedback>
    
  );
}
