import { useState } from 'react';
import './model-config.css';

const ModelConfig = () => {
    let [ sliderValue, setSliderValue ] = useState(0.5);



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

    const [layerSizes, setLayerSizes] = useState([]);
    const [currentSize, setCurrentSize] = useState(0);

    const changeSize = (e) => {
        setCurrentSize(e.target.value);
    }

    const addLayerSize = () => {
        if(currentSize > 0) {
            setLayerSizes(layerSizes.concat(currentSize));
        }
        console.log(layerSizes);
    }

    const modelSizeConfig = (
        <div className={'activation-selector-container'}>
            <div style={{ paddingTop: "10px" }}></div>
            <div className={'activation-layers-window'}>
                {layerSizes.map((str, idx) => <p>&nbsp; Layer {idx+1} Nodes: <b>{str}</b></p>)}
            </div>
            <div style={{height:"3px", backgroundColor: "#404049"}}></div>
            <input type={'number'} onChange={changeSize}/>
            <label htmlFor={'select-modelSize-button'} className={'select-activation-label'}><b>+</b> Add</label>
            <button id={'select-modelSize-button'} onClick={ addLayerSize }></button>
        </div>
    )

    const [trainingDatasetSize, setTrainingDatasetSize] = useState(0);
    const [yColumnSize, setYColumnSize] = useState(0);

    const setDatasetSizeOnChange = (isTrain) => (e) => {
        if(isTrain) {
            setTrainingDatasetSize(e.target.value);
            console.log(trainingDatasetSize)
        } else {
            setYColumnSize(e.target.value);
            console.log(isTrain)
        }
    }


    const datasetSize = (
        <div className={'dataset-size-selection'}>
            <div style={{paddingTop: '10px'}}></div>
            <p style={{textAlign: 'center'}}><b>Training Dataset Size:</b></p>
            <input type={'text'} onChange={setDatasetSizeOnChange(true)}/>
            <div style={{paddingTop: '10px'}}></div>
            <p style={{textAlign: 'center'}}><b>Label Size:</b></p>
            <input type={'text'} onChange={setDatasetSizeOnChange(false)}/>
            <div style={{paddingBottom: ''}}></div>
        </div>
    );

    const modelConfigSubmission = async () => {
        const body = {
            submitted: true,
            modelSize: layerSizes,
            layerActivations: layerActivations,
            modelLoss: selectedLoss,
            testTrainSplit: sliderValue,
            dataSetShape: trainingDatasetSize,
            yColumnSize: yColumnSize,
            zScoreVal: zScoreVar,
            minMaxVal: minMaxVar,
            oneHotVal: oneHotVar,
            epochs: epoch,
            lr: lr
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
    let [ zScoreVar, setZScoreVar ] = useState(false);
    let [ minMaxVar, setMinMaxVar ] = useState(false);
    let [ oneHotVar, setOneHotVar ] = useState(false);
    const onZScoreChange = (e) => { setZScoreVar(e.target.checked); }
    const onMinMaxChange = (e) => { setMinMaxVar(e.target.checked); }
    const onOneHotChange = (e) => { setOneHotVar(e.target.checked); }

    const scores = (
        <div className={'z-score-normalisation'}>
            <input type={'checkbox'} onChange={onZScoreChange}/> <b>Normalise data (Z-Score)</b>
            <input type={'checkbox'} onChange={onMinMaxChange}/> <b>Normalise data (MinMax)</b> {/*MUST ADD TEST*/}
            <input type={'checkbox'} onChange={onOneHotChange}/> <b>Encode data (One-Hot)</b>
        </div>
    )

    const [epoch, setEpoch] = useState(0);

    const onEpochChange = (e) => {
        setEpoch(e.target.value);
    }

    const [lr, setLr] = useState(0);

    const onLrChange = (e) => {
        setLr(e.target.value);
    }

    const epochsLearningRate = (
        <div className={'epoch-entry z-score-normalisation'}>
            <b>Number of Epochs:</b>
            <input type={'number'} onChange={onEpochChange}/>

            <b>Learning Rate:</b>
            <input type={'number'} onChange={onLrChange}/>
        </div>
    )

    const [selectedLoss, setSelectedLoss] = useState("");
    const modifyLoss = (e) => { // TODO: Change name!
        let lossTarget = e.target.value.substring(3);
        if(lossTarget !== "Select Loss Function...") {
            setSelectedLoss(lossTarget);
        }
    }

    const modelLoss = (
        <div className={'select-model-loss'}>
            <b> </b>
            <div className={'activation-selector-container'}>
                <select className={'select-activation'} onChange={ modifyLoss }>
                    <option>&nbsp;&nbsp;&nbsp;Select Loss Function...</option>
                    <option>&nbsp;&nbsp;&nbsp;SSE</option>
                    <option>&nbsp;&nbsp;&nbsp;CategoricalCrossEntropyWithSoftmax</option>
                </select>
            </div>
        </div>
    )
    return (
        <>
            {trainTestSlider}
            {activationSelector}
            {modelSizeConfig}
            {datasetSize}
            {scores}
            {epochsLearningRate}
            {modelLoss}
            {submitModelConfigButton}
        </>
    )
}

export default ModelConfig;