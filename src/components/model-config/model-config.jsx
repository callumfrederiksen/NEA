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

    const [ layerActivations, setLayerActivations ] = useState(["ReLU", "ReLU", "Sigmoid"]);



    const activationSelector = (
        <div className={'activation-selector-container'}>
            <div style={{ paddingTop: "10px" }}></div>
            <div className={'activation-layers-window'}>
                {layerActivations.map((str, idx) => <p>&nbsp; Layer {idx+1}: <b>{str}</b></p>)}
            </div>
        </div>
    )

    return (
        <>
            {trainTestSlider}
            {activationSelector}
        </>
    )
}

export default ModelConfig;