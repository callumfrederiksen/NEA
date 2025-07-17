import React, { useState } from 'react';
import './data-pre-processing.css';

function DataPreProcessing() {
    const [file, setFile] = useState(null);

    function handleFile(e) {
        setFile(e.target.files[0]);
    }

    const fileUpload = async () => {
        if(file) {
            console.log('uploading file...')
            const formData = new FormData();
            formData.append(
                'file',
                file
            );

            await fetch('http://localhost:3001/upload', {
                method: 'POST',
                body: formData
            });
            alert("Uploaded");
        }
    }

    return (
        <div className={'main-column'}>
        <input type={'file'} onChange={ handleFile }/>
        <button onClick={ fileUpload} >Upload</button>
        </div>
    );
}

export default DataPreProcessing;