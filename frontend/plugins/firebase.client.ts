import firebase from "firebase/app";
import "firebase/analytics";
import { FirebaseConfig } from '~/models/types';

export default defineNuxtPlugin(nuxtApp => {
  if (import.meta.env.VITE_APIVAULT_APP_MODE === 'dev') {
    return;
  }

  const firebaseConfig: FirebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_APIKEY,
    authDomain: import.meta.env.VITE_FIREBASE_AUTHDOMAIN,
    projectId: import.meta.env.VITE_FIREBASE_PROJECTID,
    storageBucket: import.meta.env.VITE_FIREBASE_STORAGEBUCKET,
    messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGINGSENDERID,
    appId: import.meta.env.VITE_FIREBASE_APPID,
    measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENTID,
  };

  console.log(firebaseConfig);

  firebase.initializeApp(firebaseConfig);
  firebase.analytics()
})