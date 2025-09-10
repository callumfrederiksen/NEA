import UploadButton from './components/upload-button.jsx';
import ColumnSelector from './components/column-selector.jsx';
import SelectYValue from './components/select-y-value.jsx';
import TrainButton from './components/train-button.jsx';
import ModelConfig from '../model-config/model-config.jsx';

import { useState } from 'react';

import './data-pre-processing.css';

const DataPreProcessing = () => {
    const [ displayConfigs, setDisplayConfigs ] = useState(false); // change

    const switchDisplayConfigsON = () => {
        setDisplayConfigs(true);
    }

    const switchDisplayConfigsOFF = () => {
        setDisplayConfigs(false);
    }

    if(displayConfigs) { // Conditional rendering
        return (
            <div className={'main-column main-column-properties'}>
                <div><p className={'display-none-1'}>HEADING</p></div>
                <div className={'back-config-button-container'}>
                    <label htmlFor={'back-config-button'} className={'back-config-button-label'}><b> &lt; &nbsp;</b> Back</label>
                    <button id={'back-config-button'} onClick={ switchDisplayConfigsOFF }></button>
                </div>

                <ModelConfig />
            </div>
        )
    } else {
        return (
            <div className={'main-column main-column-properties'}>
                <p style={{'textAlign': 'center', 'paddingTop': '10%'}}><b>Upload Dataset:</b></p>
                <UploadButton/>

                <p style={{'textAlign': 'center', 'paddingTop': '8%'}}><b>Columns in Dataset:</b></p>
                <ColumnSelector/>

                <p style={{'textAlign': 'center', 'paddingTop': '7%'}}><b>Select the Y Column:</b></p>
                <SelectYValue/>

                { /* This next button will set displayConfigs to true, in order to change the model configurations */ }
                <div className={'config-button-container'}>
                    <label htmlFor={'config-button'} className={'config-button-label'}><b>Model Configurations</b></label>
                    <button id={'config-button'} onClick={ switchDisplayConfigsON }></button>
                </div>

                <TrainButton/>

            </div>
        )
    }
}

export default DataPreProcessing;