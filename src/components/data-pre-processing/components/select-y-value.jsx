import React, {useState, useEffect} from 'react';
import '../data-pre-processing.css';

function SelectYValue() {
    const [columns, setColumns] = useState([]);
    const [ yTarget, setYTarget ] = useState("");

    useEffect(() => {
        const fetchColumns = async () => {
            const response  = await fetch('http://localhost:8443/return-column-selector');
            const data = await response.json();
            setColumns(data.columns)
        }
        fetchColumns();
    }, [])



    const selectOnChange = (e) => {
        let currentValue = e.target.value;
        currentValue = currentValue.slice(2);
        setYTarget(currentValue);
    }

    const submitOnClick = async () => {
        const body = { yColumnName: yTarget };

        const response = fetch("http://localhost:8443/select-y-column", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        });
    }

    return (
        <div className={'select-y-value-container'}>
            <select className={'custom-select-1'} onChange={selectOnChange}>
                <option>&nbsp;&nbsp;Select Column...</option>
                {/*<option>Select a y-value:</option>*/}
                {columns.map((str, idx) => <option>&nbsp;&nbsp;{str}</option>)}
            </select>

            <label htmlFor={'select-y-value-button'} className={'select-y-value-label'}><b>Submit</b></label>
            <button id={'select-y-value-button'} onClick={submitOnClick}></button>

        </div>
    )
}

export default SelectYValue;