import React, { useState, useEffect } from 'react';
import '../data-pre-processing.css';

function ColumnSelector() {
    const [columns, setColumns] = useState([]);

    useEffect(() => {
        const fetchColumns = async ()=> {
            let response = await fetch('http://localhost:8443/return-column-selector')
            const data = await response.json();
            setColumns(data.columns);
        }
        fetchColumns();
    }, [])


    return (
        <div className={'column-selector-container'}>
            {columns.map(str => <p className={'text-columns'}>{str}</p>)}
        </div>
    )
}

export default ColumnSelector;