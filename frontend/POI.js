import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image } from 'react-native';
import {useState, useEffect} from 'react'
import { BLUE, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_YELLOW, RED, YELLOW } from './CONSTANTS';
import {TITLE, IMGURL, DESC, WORDLE_WORDS} from './dummy'
import { getToken } from './Utils';


export default function Home({route, navigation}) {
  
  const [title, setTitle] = useState('');
  const [imgurl, setImgurl] = useState('');
  const [image, setImage] = useState(null);
  const [desc, setDesc] = useState('')
  const [stringOfWordleWords, setStringOfWordleWords] = useState('')
  const [wordleWords, setWordleWords] = useState('')
  // TODO: change to an array of wordle words, handle it inside data

  async function getPOI(poi_id) {
    const user_token = await getToken('token')
    const res = await fetch(`https://b723-223-139-248-33.ngrok-free.app/api/v1/poi/${poi_id}` , {
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
      setDesc(data.description_en)
      setStringOfWordleWords(data.keywords)
    } catch (e) {
      console.log('Error: ' + e)
    }
  }

  async function getImage() {
    const user_token = await getToken('token')
    const res = await fetch(`https://b723-223-139-248-33.ngrok-free.app/api/v1/poi/image/${imgurl}` , {
      method: 'GET',
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${user_token}`,
      },
    })

    const data = await res.json()

    try {
      setImage(data)
      
    } catch (e) {
      console.log('Error: ' + e)
    }
  }

  useEffect(() => {
    const id = route.params.id
    getPOI(id)
    if(imgurl!='') getImage()
    if(stringOfWordleWords!='') setWordleWords(stringOfWordleWords.split(','))
  }, [imgurl,stringOfWordleWords])
  

  return !image ? <View style={styles.loading}><Text style={{fontSize: 20}}>Loading...</Text></View>: (
    <View style={styles.container}>
      <View>
        <Text style={styles.title}>{title}</Text>
      </View>


      <Image 
        source={{uri: image}}
        style={styles.imageContainer}
      />
      
      <View>
       <Text style={styles.desc}>{desc}</Text>
      </View>

      <TouchableOpacity style={styles.btn} onPress={() => {
          navigation.navigate('Wordle', {words: wordleWords})
        }}>
        <Text style={styles.btnText}>Play Wordle!</Text>
      </TouchableOpacity>

    </View>
    
  );
}

const styles = StyleSheet.create({
  loading: {
    backgroundColor: LIGHT_GREEN,
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center'
  },
  container: {
    flex: 1,
    backgroundColor: LIGHT_GREEN,
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
    fontSize: 16
  },
  imageContainer: {
    width: 290, 
    height: 240,
    borderRadius: 5,
    borderWidth: 0.5,

  },  
  btn: { 
    width: "80%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 30,
    backgroundColor: GREEN,
  },
  btnText: {
    color: "white",
    fontWeight: "bold", 
    fontSize: 24
  }
});
