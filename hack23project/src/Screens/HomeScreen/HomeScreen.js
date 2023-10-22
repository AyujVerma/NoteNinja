import React, { useState } from 'react';
import './HomeScreen.css';
import Slides from "../../Components/Slides/slides.js";
import Audio from "../../Components/Audio/audio.js";
import logo from "../HomeScreen/image-removebg-preview.png"

const HomeScreen = () => {
  const [filesSlides, setFilesSlides] = useState([]); // State for lecture slides
  const [filesAudio, setFilesAudio] = useState([]);   // State for audio

  const handleGenerateClick = () => {
    // Implement the generate functionality here
    // You can use filesSlides and filesAudio to generate something
    // For example, you can create a function that combines the data from these files.
  };

  return (
    <div className="home-screen">
      <div className="top-bar">
        <img src={logo} alt='logo' style={{width: "20%", marginTop: "2%"}}/>
      </div>
      <div className="blurb">slicing up the slides.</div>
      <div className="box">
        <div className="components-container">
          <Slides onFilesSelected={setFilesSlides} width="300px" height='190px'/>
          <Audio onFilesSelected={setFilesAudio} width="300px" height='190px'/>
        </div>
        <div className="generate-button-container">
          <button onClick={handleGenerateClick} className="generate-button" style={{ fontFamily: 'DM Sans, sans-serif'}}>Generate</button>
        </div>
      </div>
    </div>
  );
};

export default HomeScreen;
