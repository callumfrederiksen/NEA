import { useState, useEffect } from 'react';
import lossImage from "../../uploads/losses.png";

import './metrics-window.css';

const MetricsWindow = () => {
    let [data, setData] = useState("");
    useEffect(() => {
        const rtrn = async () => {
            const res = await fetch("http://localhost:8443/get-returned-metrics")
            setData(await res.json());
            await console.log(data.accuracyMetric);
        }
        rtrn();
    }, []);

    return (
        <div className={'metrics-window'}>
            <br/>
            <b><p>&nbsp;&nbsp;&nbsp;Loss Image:</p></b>
            <br />
            &nbsp;&nbsp;&nbsp;<img src={lossImage} style={{'width': '80%', 'height': '600px', 'textAlign': 'center'}}/>
            <br/>&nbsp;
            <a href="http://localhost:8443/download-parameters-weights" style={{ zIndex: 9999, pointerEvents: 'auto' }}>Download Weights</a>
            <a href="http://localhost:8443/download-parameters-biases" style={{ zIndex: 9998, pointerEvents: 'auto' }}>Download Biases</a>
            <div>
                <p>Test Accuracy: {data.accuracyMetric}</p>
            </div>
        </div>
    );
}

export default MetricsWindow;