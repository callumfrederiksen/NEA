import React, {useState, useEffect} from 'react';
import '../data-pre-processing.css';

function SelectYValue() {
    const [columns, setColumns] = useState([]);

    useEffect(() => {
        const fetchColumns = async () => {
            const response  = await fetch('http://localhost:8443/return-column-selector');
            const data = await response.json();
            setColumns(data.columns)
        }
        fetchColumns();
    }, [])

    return (
        <div className={'select-y-value-container'}>
            <select className={'custom-select-1'}>
                <option>&nbsp;&nbsp;Select Column...</option>
                {/*<option>Select a y-value:</option>*/}
                {columns.map((str, idx) => <option>&nbsp;&nbsp;{idx+1}. {str}</option>)}
            </select>
        </div>
    )
}

export default SelectYValue;