import UploadButton from './components/upload-button.jsx';
import ColumnSelector from './components/column-selector.jsx';
import SelectYValue from './components/select-y-value.jsx';

const DataPreProcessing = () => {
    return (
        <div className={'main-column main-column-properties'}>
            <UploadButton />

            <p style={{'text-align': 'center', 'padding-top': '10%'}}><b>Columns in Dataset:</b></p>
            <ColumnSelector/>

            <p style={{'text-align': 'center', 'padding-top': '5%'}}><b>Select the Y Column:</b></p>
            <SelectYValue />

        </div>
    )
}

export default DataPreProcessing;