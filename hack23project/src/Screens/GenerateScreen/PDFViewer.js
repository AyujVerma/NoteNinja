import React from 'react';
import './PDFViewer.css';

const PDFViewer = ({ pdfUrl }) => {
  return (
    <iframe
      title="PDF Viewer"
      src={pdfUrl}
      width="45%"
      height="700"
      className="centered-pdf"
      
    />
  );
};

export default PDFViewer;
