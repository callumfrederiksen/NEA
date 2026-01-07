import { useState, useEffect } from 'react';
import lossImage from "../../uploads/losses.png";

import './metrics-window.css';

const MetricsWindow = () => {
    return (
        <div className={'metrics-window'}>
            <br/>
            <b><p>&nbsp;&nbsp;&nbsp;Loss Image:</p></b>
            <br />
            &nbsp;&nbsp;&nbsp;<img src={lossImage} style={{'width': '80%', 'height': '600px', 'textAlign': 'center'}}/>
            <br/>&nbsp;
            <a href="http://localhost:8443/download-parameters" style={{ zIndex: 9999, pointerEvents: 'auto' }}>Download</a>
        </div>
    );
}

export default MetricsWindow;