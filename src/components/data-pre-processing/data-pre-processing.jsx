import UploadButton from './components/upload-button.jsx';
import ColumnSelector from './components/column-selector.jsx';
import SelectYValue from './components/select-y-value.jsx';
import TrainButton from './components/train-button.jsx';
const DataPreProcessing = () => {
    return (
        <div className={'main-column main-column-properties'}>
            <UploadButton />

            <p style={{'textAlign': 'center', 'paddingTop': '10%'}}><b>Columns in Dataset:</b></p>
            <ColumnSelector/>

            <p style={{'textAlign': 'center', 'paddingTop': '5%'}}><b>Select the Y Column:</b></p>
            <SelectYValue />

            <TrainButton />

        </div>
    )
}

export default DataPreProcessing;