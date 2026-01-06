import '../data-pre-processing.css';

const TrainButton = () => {
    const onClick = async () => {
        const body = {
            submitted: true
        }

        const response = fetch("http://localhost:8443/run", {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });
    }

    return (
        <div className={'submit-button-container'}>
            <label htmlFor={'submit-button'} className={'submit-button-label'}><b>Submit</b></label>
            <button id={'submit-button'} onClick={ onClick }></button>
        </div>
    )
}

export default TrainButton;