import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image } from 'react-native';
import {useState, useEffect} from 'react'
import { BLUE, LIGHT_BLUE, LIGHT_YELLOW, RED, YELLOW } from './CONSTANTS';
import {TITLE, IMGURL, DESC, WORDLE_WORDS} from './dummy'
import { getToken } from './Utils';


export default function Home({route, navigation}) {
  

  const [title, setTitle] = useState('');
  const [imgurl, setImgurl] = useState('');
  const [desc, setDesc] = useState('')
  const [stringOfWordleWords, setStringOfWordleWords] = useState('')
  // TODO: change to an array of wordle words, handle it inside data

  async function getPOI(poi_id) {
    const user_token = await getToken('token')
  
    const res = await fetch('https://efce-223-139-248-33.ngrok-free.app/api/v1/poi/3' , {
      method: 'GET',
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${user_token}`,
      },
    })

    const data = await res.json()

    try {
      setTitle(data.poiTitle)
      setImgurl(data.image_url)
      setDesc(data.description)
      setStringOfWordleWords(data.keywords)
    } catch (e) {
      console.log('Error: ' + e)
    }
  }

  useEffect(() => {
    const id = route.params.id
    getPOI(id)
  }, [])
  

  return (
    <View style={styles.container}>
      <View>
        <Text style={styles.title}>{title}</Text>
      </View>

      {/* <Image source={imgurl} style={styles.imageContainer} /> */}

      <Image 
        source={{uri: 'https://engineering.fb.com/wp-content/uploads/2016/04/yearinreview.jpg'}}
        style={styles.imageContainer}
      />
      {/* <Image source={{uri: ''}} /> 
       FOR FUTURE REFERENCE */}
      
      <View>
       <Text style={styles.desc}>{desc}</Text>
      </View>

      <TouchableOpacity style={styles.btn} onPress={() => {
          navigation.navigate('Wordle', {words: wordle})
        }}>
        <Text style={styles.btnText}>Play Wordle!</Text>
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
    paddingTop: 30
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    paddingBottom: 24,
  },
  desc: {
    marginTop: 30,
    marginRight: 40,
    marginLeft: 40,
    textAlign: 'center',
    fontSize: 16
  },
  imageContainer: {
    width: 300, 
    height: 250,
    borderRadius: 5,
    borderWidth: 0.5,

  },  
  btn: { 
    width: "80%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
    backgroundColor: BLUE,
  },
  btnText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 24
  }
});
