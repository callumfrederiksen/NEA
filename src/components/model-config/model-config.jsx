import { useState } from 'react';
import './model-config.css';

const ModelConfig = () => {
    let [ sliderValue, setSliderValue ] = useState(0.5);
    const onSliderChange = (e) => {
        setSliderValue(e.target.value / 100);
    }

    return (
        <div className={'form-container'}>
            <form>
                <div className={'slider-container'}>
                    <input className={'slider-input'} type={'range'} onChange={ onSliderChange }/>
                    <p className={'train-test-split-display'}><b>{Math.round(sliderValue*100)}% </b> train, <b>{Math.round((1-sliderValue)*100)}% </b> test </p>
                </div>
            </form>
        </div>
    )
}

export default ModelConfig;