import UploadButton from './components/upload-button.jsx';
import ColumnSelector from './components/column-selector.jsx';
import SelectYValue from './components/select-y-value.jsx';

const DataPreProcessing = () => {
    return (
        <div className={'main-column main-column-properties'}>
            <UploadButton />
            <ColumnSelector/>
            <SelectYValue />
        </div>
    )
}

export default DataPreProcessing;