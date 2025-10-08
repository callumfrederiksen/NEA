import '../data-pre-processing.css';

const TrainButton = () => {
    const onClick = async () => {
        const body = {
            submitted: false,
            modelSize: [784, 256, 128, 10],
            layerActivations: ["ReLU", "ReLU", "Softmax"],
            modelLoss: "CategoricalCrossEntropyWithSoftmax"
        }

        const response = fetch("http://localhost:8443/submit-hyperparameters", {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });
        console.log(response)
    }

    return (
        <div className={'submit-button-container'}>
            <label htmlFor={'submit-button'} className={'submit-button-label'}><b>Submit</b></label>
            <button id={'submit-button'} onClick={ onClick }></button>
        </div>
    )
}

export default TrainButton;