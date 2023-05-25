import * as SecureStore from 'expo-secure-store';

export async function setToken(key, value) {
  try {
    await SecureStore.setItemAsync(key, String(value));
  } catch (e) {
    console.log("error: " + e)
  }
}

export async function deleteToken(key) {
  try {
    await SecureStore.deleteItemAsync(key)
  } catch (e) {
    console.log("delete token error: " + e)
  }
}

export async function getToken(key) {
  try {
    return await SecureStore.getItemAsync(key);
  } catch (e) {
    console.log("error: " + e)
    return null
  }
}