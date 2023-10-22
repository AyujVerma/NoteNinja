// audio.js

import React, { useEffect, useState } from "react";
import { AiOutlineCheckCircle, AiOutlineCloudUpload } from "react-icons/ai";
import { MdClear } from "react-icons/md";
import "./audio.css";

const Audio = ({
  onFilesSelected: onFilesSelectedAudio,
  width,
  height,
}) => {
  const [filesAudio, setFilesAudio] = useState([]);

  const handleFileChangeAudio = (event) => {
    const selectedFiles = event.target.files;
    if (selectedFiles && selectedFiles.length > 0) {
      const newFiles = Array.from(selectedFiles);
      setFilesAudio((prevFiles) => [...prevFiles, ...newFiles]);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const droppedFiles = event.dataTransfer.files;
    if (droppedFiles.length > 0) {
      const newFiles = Array.from(droppedFiles);
      setFilesAudio((prevFiles) => [...prevFiles, ...newFiles]);
    }
  };

  const handleRemoveFile = (index) => {
    setFilesAudio((prevFiles) => prevFiles.filter((_, i) => i !== index));
  };

  useEffect(() => {
    onFilesSelectedAudio(filesAudio);
  }, [filesAudio, onFilesSelectedAudio]);

  return (
    <section className="drag-drop" style={{ width: width, height: height }}>
      <div
        className={`document-uploader ${filesAudio.length > 0 ? "upload-box active" : "upload-box"
        }`}
        onDrop={handleDrop}
        onDragOver={(event) => event.preventDefault()}>
          <div className="upload-info">
            <div>
              <p style={{ marginBottom: '5px', fontSize: "26px", fontFamily: 'DM Sans, sans-serif'}}>Audio</p>
            </div>
            <AiOutlineCloudUpload style={{ marginBottom: '0px', fontSize: "128px", color: "#dfebf8" }} />
            <p style={{marginBottom: '5px', color: '#dfebf8'}} >.WAV Only</p>
          </div>
          <input
            type="file"
            hidden
            id="browse"
            onChange={handleFileChangeAudio}
            accept=".wav"
          />
          {filesAudio.length === 0 && (  // Conditional rendering for the button
            <label htmlFor="browse" className="browse-btn" style={{ fontFamily: 'DM Sans, sans-serif'}}>
              Choose File
            </label>
          )}

          {filesAudio.length > 0 && (
            <div className="file-list">
              <div className="file-list__container">
                {filesAudio.map((file, index) => (
                  <div className="file-item" key={index}>
                    <div className="file-info">
                      <p>{file.name}</p>
                      {/* <p>{file.type}</p> */}
                    </div>
                    <div className="file-actions">
                      <MdClear onClick={() => handleRemoveFile(index)} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {filesAudio.length > 0 && (
            <div className="success-file">
              <AiOutlineCheckCircle
                style={{marginRight: 1 }}
              />
              <p>{filesAudio.length} file selected</p>
            </div>
          )}
        </div>
      </section>
    );
};

export default Audio;
