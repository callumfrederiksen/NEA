import UploadButton from './components/upload-button.jsx';
import ColumnSelector from './components/column-selector.jsx';

const DataPreProcessing = () => {
    return (
        <div className={'main-column main-column-properties'}>
            <UploadButton />
            <ColumnSelector/>

        </div>
    )
}

export default DataPreProcessing;