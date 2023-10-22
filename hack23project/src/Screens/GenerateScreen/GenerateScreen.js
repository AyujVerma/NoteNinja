import React, { useEffect, useState } from 'react';
import './GenerateScreen.css';
import logo from '../../assets/image-removebg-preview.png';
import PDFViewer from './PDFViewer';
import { getDownloadURL, ref, getStorage, deleteObject } from 'firebase/storage'; // Import the Firebase Storage functions
import { storage } from '../../firebase.js';

const GenerateScreen = () => {
    const [pdfUrl, setPdfUrl] = useState(null); // State to store the PDF download URL
    const [refreshed, setRefreshed] = useState(false); // State to track if the page has been refreshed

    useEffect(() => {

        // // Create a reference to the file to delete
        // const desertRef = ref(storage, 'output.pdf');

        // // Delete the file
        // deleteObject(desertRef).then(() => {
        // // File deleted successfully
        // }).catch((error) => {
        // // Uh-oh, an error occurred!
        // });

        // Fetch the download URL for the PDF from Firebase Storage
        const storagePath = 'output.pdf'; // Replace with your file path
        const pdfStorageRef = ref(storage, storagePath); // Create a reference to your PDF

        // Get the download URL and set it in the state
        getDownloadURL(pdfStorageRef)
            .then((url) => {
                setPdfUrl(url);
            })
            .catch((error) => {
                console.error('Error getting download URL: ', error);
            });
    }, []);

    useEffect(() => {
        if (!refreshed) {
            const pdfPath = 'output/output.pdf';

            const checkPDFExistence = async () => {
                try {
                    const response = await fetch(pdfPath);
                    if (response.status === 200) {
                        setRefreshed(true);
                        console.log('Refreshed.');
                        window.location.reload();
                    }
                    else {
                        const intervalId = setInterval(checkPDFExistence, 15000);
                        return () => {
                            clearInterval(intervalId);
                        };
                    }
                } catch (error) {
                    console.error('Error checking PDF existence: ', error);
                }
            };
        }
    }, [refreshed]);

    return (
        <div className="generate-screen">
            <div className="top-bar">
                <img src={logo} alt="logo" style={{ width: '20%', marginTop: '2%' }} />
            </div>
            <div className="blurb">sharp notes for sharper students.</div>
            {pdfUrl ? (
                <PDFViewer pdfUrl={pdfUrl} />
            ) : (
                <p className="load-text">slicing the presentation...</p>

            )}
        </div>
    );
};

export default GenerateScreen;