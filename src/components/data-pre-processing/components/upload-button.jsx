import React, { useState } from 'react';
import '../data-pre-processing.css';

function UploadButton() {
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
        }
    }

    return ( // https://stackoverflow.com/questions/572768/styling-an-input-type-file-button
        <div className={'main-column-properties upload-section'}>
            <label htmlFor={'upload-input'} className={'file-input-label'}>
                Upload File
            </label>
            <input id={'upload-input'} type={'file'} onChange={ handleFile } />
            <button className={'upload-button'} onClick={ fileUpload } >Upload</button>
        </div>
    );
}

export default UploadButton;