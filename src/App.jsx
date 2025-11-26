import Header from './components/header/header.jsx';
import DataPreProcessing from './components/data-pre-processing/data-pre-processing.jsx';
import MetricsWindow from './components/metrics-window/metrics-window.jsx';

import React, {useState, useEffect} from 'react';
import './index.css';

function App() {
    useEffect(() => {
        const rtrn = async () => {
            const res = await fetch("http://localhost:8443/get-returned-metrics")
            const data = await res.json()
            await console.log(data.accuracyMetric);
        }
        rtrn();
    }, []);

    return (
      <>
      <Header />
      <MetricsWindow />
      <DataPreProcessing />


      </>
    );
}

export default App;
