// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import {getStorage} from "firebase/storage"

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAsgqPo8k4jxrtHHLgJs--E1wEXYNZ6FUU",
  authDomain: "hacktx2023-402718.firebaseapp.com",
  projectId: "hacktx2023-402718",
  storageBucket: "hacktx2023-402718.appspot.com",
  messagingSenderId: "160481126529",
  appId: "1:160481126529:web:55b70ff27493a477464580"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app)