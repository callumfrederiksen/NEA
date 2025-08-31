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
            <div style={{height:"3px", backgroundColor: "#404049"}}></div>
            <div className={'select-activation-container'}>
                <select className={'select-activation'}>
                    <option>&nbsp;&nbsp;&nbsp;Select Activation...</option>
                    <option>&nbsp;&nbsp;&nbsp;Sigmoid</option>
                    <option>&nbsp;&nbsp;&nbsp;ReLU</option>
                    <option>&nbsp;&nbsp;&nbsp;SoftMax</option>
                </select>
                <label htmlFor={'select-activation-button'} className={'select-activation-label'}><b>+</b> Add</label>
                <button id={'select-activation-button'}></button>
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