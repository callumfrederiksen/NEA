import Header from './components/header/header.jsx';
import DataPreProcessing from './components/data-pre-processing/data-pre-processing.jsx';
import ModelHyperparameterSelection from './components/popups/model-hyperparameter-selection.jsx';


import React, {useState, useEffect} from 'react';
import './index.css';

function App() {
    const { displayModelHyperparameterSelection, setDisplayModelHyperparameterSelection } = useState(false);

    return (
      <>
      <ModelHyperparameterSelection/>
      { displayModelHyperparameterSelection : <p>hi</p> ? <p>bye</p> }
      <Header />
      <DataPreProcessing />

      </>
    );
}

export default App;

