// const admin = require('firebase-admin');
const fs = require('fs');

var serviceAccount = require("./maelisteningtest-firebase-adminsdk-9gwa6-110afb45b7.json");

var admin = require("firebase-admin");

// admin.initializeApp({
//     apiKey: "AIzaSyD7y9iBRvyxim9_9l8m5LQRexBdB63cmHo",
//     authDomain: "maelisteningtest.firebaseapp.com",
//     projectId: "maelisteningtest",
//     storageBucket: "maelisteningtest.appspot.com",
//     messagingSenderId: "953894482343",
//     appId: "1:953894482343:web:a505e13240e8ea5dac0682",
//     measurementId: "G-F2RS4PDMKP"
// });

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
  });

const db = admin.firestore();
const collectionRef = db.collection('Results_Test_1');

collectionRef.get()
  .then((snapshot) => {
    const data = [];
    snapshot.forEach((doc) => {
      data.push(doc.data());
    });

    const jsonData = JSON.stringify(data);
    fs.writeFileSync('./output/exportedData.json', jsonData);
    console.log('Dati esportati correttamente!');
  })
  .catch((error) => {
    console.error('Errore durante l\'esportazione dei dati:', error);
  });