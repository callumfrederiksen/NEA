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

            await fetch('https://trainable.studio:8443/upload', {
                method: 'POST',
                body: formData
            });
        }
    }

    return ( // https://stackoverflow.com/questions/572768/styling-an-input-type-file-button
        <div className={'upload-section'}>
            <label htmlFor={'upload-input'} className={'upload-input-label'}>
                Upload File
            </label>
            <input id={'upload-input'} type={'file'} onChange={ handleFile } />
            <label htmlFor={'upload-button'} className={'upload-button-label'}>
                <b>Upload</b>
            </label>
            <button id={'upload-button'} onClick={ fileUpload }></button>
        </div>
    );
}

export default UploadButton;
