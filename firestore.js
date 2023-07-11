import firebase from 'firebase/app';
import { getFirestore , collection, getDocs, doc, setDoc} from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyD7y9iBRvyxim9_9l8m5LQRexBdB63cmHo",
  authDomain: "maelisteningtest.firebaseapp.com",
  projectId: "maelisteningtest",
  storageBucket: "maelisteningtest.appspot.com",
  messagingSenderId: "953894482343",
  appId: "1:953894482343:web:a505e13240e8ea5dac0682",
  measurementId: "G-F2RS4PDMKP"
};

// Inizializza l'app Firebase
firebase.initializeApp(firebaseConfig);

// Ottieni istanza di Firestore
const db = getFirestore();


const colRef = collection(db, 'results');


getDocs(colRef)
  .then((snapshot) => {
    console.log(snapshot.docs)
  });

