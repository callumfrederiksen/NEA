import '../data-pre-processing.css';


const TrainButton = () => {
    return (
        <div className={'submit-button-container'}>
            <label htmlFor={'submit-button'} className={'submit-button-label'}><b>Submit</b></label>
            <button id={'submit-button'}></button>
        </div>
    )
}

export default TrainButton;