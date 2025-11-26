import { useState, useEffect } from 'react';
import lossImage from "../../uploads/losses.png";

import './metrics-window.css';

const MetricsWindow = () => {
    return (
        <div className={'metrics-window'}>
            <b><p>Loss Image:</p></b>
            <br />
            <img src={lossImage} style={{'width': '80%', 'height': '600px', 'textAlign': 'centre'}}/>
        </div>
    );
}

export default MetricsWindow;