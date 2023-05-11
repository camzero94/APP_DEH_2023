import * as SecureStore from 'expo-secure-store';

export async function setToken(key, value) {
  try {
    await SecureStore.setItemAsync(key, value);
  } catch (e) {
    console.log("error: " + e)
  }
}
