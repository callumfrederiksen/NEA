import React, { useState } from 'react';
const express = require('express');
const cors = require('cors');

const port = 8443;

const app = express();
app.use(cors());


function ColumnSelector() {
    const [columns, setColumns] = useState(null);

    app.post('/response1', (req, res) => {
        console.log(req);
        setColumns(req)
    })

    return (
        <>{columns}</>
    )
}

export default ColumnSelector;