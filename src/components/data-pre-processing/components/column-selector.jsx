import React, { useState, useEffect } from 'react';

function ColumnSelector() {
    const [columns, setColumns] = useState([]);

    useEffect(() => {
        const fetchColumns = async ()=> {
            let response =  await fetch('http://localhost:8443/return-column-selector')
            const data = await response.json();
            setColumns(data.columns);
            console.log(data.columns)
        }
        fetchColumns();
    }, [])


    return (
        <>{columns.map(str => <p>{str}</p>)}</>
    )
}

export default ColumnSelector;