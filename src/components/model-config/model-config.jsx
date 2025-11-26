import { useState } from 'react';
import './model-config.css';

const ModelConfig = () => {
    let [ sliderValue, setSliderValue ] = useState(0.5);
    let [ zScoreVar, setZScoreVar ] = useState(false);

    const onZScoreChange = (e) => {
        if(zScore) {
            setZScoreVar(true);
        } else {
            setZScoreVar(false);
        }
    }
    const onSliderChange = (e) => {
        setSliderValue(e.target.value / 100);
    }

    const trainTestSlider = (
        <div className={'form-container'}>
            <form>
                <div className={'slider-container'}>
                    <p className={'train-test-split-display '}><b>Select The Test-Train Split:</b></p>
                    <input className={'slider-input'} type={'range'} onChange={ onSliderChange }/>
                    <p className={'train-test-split-display'}><b>{Math.round(sliderValue*100)}% </b> train, <b>{Math.round((1-sliderValue)*100)}% </b> test </p>
                </div>
            </form>
        </div>
    )

    const [ layerActivations, setLayerActivations ] = useState([    ]);
    const [ selectedLayerActivation, setSelectedLayerActivation ] = useState("");

    const selectedActivation = (e) => {
        var removedNonBreakingSpace = e.target.value.substring(3);
        if ( removedNonBreakingSpace !== "Select Activation...") {
            setSelectedLayerActivation( removedNonBreakingSpace );
        } else {
            setSelectedLayerActivation("");
        }
    }

    const addActivation = () => {
        if(selectedLayerActivation !== "") {
            let toAdd = layerActivations.concat(selectedLayerActivation)
            setLayerActivations(toAdd);
        }
    }

    const activationSelector = (
        <div className={'activation-selector-container'}>
            <div style={{ paddingTop: "10px" }}></div>
            <div className={'activation-layers-window'}>
                {layerActivations.map((str, idx) => <p>&nbsp; Layer {idx+1}: <b>{str}</b></p>)}
            </div>
            <div style={{height:"3px", backgroundColor: "#404049"}}></div>
            <div className={'select-activation-container'} onChange={selectedActivation}>
                <select className={'select-activation'} >
                    <option>&nbsp;&nbsp;&nbsp;Select Activation...</option>
                    <option>&nbsp;&nbsp;&nbsp;Sigmoid</option>
                    <option>&nbsp;&nbsp;&nbsp;ReLU</option>
                    <option>&nbsp;&nbsp;&nbsp;SoftMax</option>
                </select>
                <label htmlFor={'select-activation-button'} className={'select-activation-label'}><b>+</b> Add</label>
                <button id={'select-activation-button'} onClick={ addActivation }></button>
            </div>
        </div>
    );

    const [trainingDatasetSize, setTrainingDatasetSize] = useState(0);
    const [testingDatasetSize, setTestingDatasetSize] = useState(0);

    const setDatasetSizeOnChange = (isTrain) => (e) => {
        if(isTrain) {
            setTrainingDatasetSize(e.target.value);
            console.log(isTrain)
        } else {
            setTestingDatasetSize(e.target.value);
            console.log(isTrain)
        }
    }


    const datasetSize = (
        <div className={'dataset-size-selection'}>
            <div style={{paddingTop: '10px'}}></div>
            <p style={{textAlign: 'center'}}><b>Training Dataset Size:</b></p>
            <input type={'number'} onChange={setDatasetSizeOnChange(true)}/>
            <div style={{paddingTop: '10px'}}></div>
            <p style={{textAlign: 'center'}}><b>Testing Dataset Size:</b></p>
            <input type={'number'} onChange={setDatasetSizeOnChange(false)}/>
            <div style={{paddingBottom: ''}}></div>
        </div>
    );

    const modelConfigSubmission = async () => {
        const body = {
            submitted: true,
            modelSize: [784, 256, 128, 10],
            layerActivations: layerActivations,
            modelLoss: "CategoricalCrossEntropyWithSoftmax",
            testTrainSplit: sliderValue,
            dataSetShape: "784,1;781,1;",
            yColumnSize: "10,1;",
            zScoreVal: zScoreVar,
        }
        console.log(body)

        const response = fetch("http://localhost:8443/submit-hyperparameters", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });
    }

    const submitModelConfigButton = (
        <div className={'submit-model-config-button-container'}>
            <label htmlFor={'submit-button-2'} className={'submit-button-2-label'}><b>Submit</b></label>
            <button id={'submit-button-2'} onClick={modelConfigSubmission}></button>
        </div>
    )

    const zScore = (
        <div className={'z-score-normalisation'}>
            <input type={'checkbox'} onChange={onZScoreChange}/> <b>Normalise data (Z-Score)</b>
        </div>
    )

    return (
        <>
            {trainTestSlider}
            {activationSelector}
            {datasetSize}
            {zScore}
            {submitModelConfigButton}

        </>
    )
}

export default ModelConfig;