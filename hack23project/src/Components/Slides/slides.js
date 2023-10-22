// slides.js

import React, { useEffect, useState } from "react";
import { AiOutlineCheckCircle, AiOutlineCloudUpload } from "react-icons/ai";
import { MdClear } from "react-icons/md";
import "./slides.css";

const Slides = ({
  onFilesSelected,
  width,
  height,
}) => {
  const [filesSlides, setFilesSlides] = useState([]);

  const handleFileChangeSlides = (event) => {
    const selectedFiles = event.target.files;
    if (selectedFiles && selectedFiles.length > 0) {
      const newFiles = Array.from(selectedFiles);
      setFilesSlides((prevFiles) => [...prevFiles, ...newFiles]);
    }
    console.log("selectedFiles: " + selectedFiles.length);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const droppedFiles = event.dataTransfer.files;
    if (droppedFiles.length > 0) {
      const newFiles = Array.from(droppedFiles);
      setFilesSlides((prevFiles) => [...prevFiles, ...newFiles]);
    }
  };

  const handleRemoveFile = (index) => {
    setFilesSlides((prevFiles) => prevFiles.filter((_, i) => i !== index));
  };

  useEffect(() => {
    console.log("selectedFiles 2");
    onFilesSelected(filesSlides);
  }, [filesSlides, onFilesSelected]);

  return (
    <section className="drag-drop-slides" style={{ width: width, height: height }}>
      <div
        className={`document-uploader-slides ${filesSlides.length > 0 ? "upload-box active" : "upload-box"
        }`}
        onDrop={handleDrop}
        onDragOver={(event) => event.preventDefault()}>
          <div className="upload-info-slides">
            <div>
              <p style={{ marginBottom: '5px', fontSize: "26px", fontFamily: 'DM Sans, sans-serif', fontWeight: 500 }}>Lecture Slides</p>
            </div>
            <AiOutlineCloudUpload style={{ marginBottom: '0px', fontSize: "128px", color: "#dfebf8" }} />
            <p style={{ marginBottom: '5px', color: '#dfebf8' }}>.PPTX Only</p>
          </div>
          <input
            type="file"
            hidden
            id="slides"
            onChange={handleFileChangeSlides}
            accept=".pdf, .pptx"
          />
          {filesSlides.length === 0 && (  // Conditional rendering for the button
            <label htmlFor="slides" className="slides-btn" style={{ fontFamily: 'DM Sans, sans-serif' }}>
              Choose File
            </label>
          )}

          {filesSlides.length > 0 && (
            <div className="file-list-slides">
              <div className="file-list__container">
                {filesSlides.map((file, index) => (
                  <div className="file-item-slides" key={index}>
                    <div className="file-info-slides">
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

          {filesSlides.length > 0 && (
            <div className="success-file">
              <AiOutlineCheckCircle
                style={{ color: "#6DC24B", marginRight: 1 }}
              />
              <p>{filesSlides.length} file selected</p>
            </div>
          )}
        </div>
      </section>
    );
};

export default Slides;
