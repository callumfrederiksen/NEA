const express = require('express');
const multer = require('multer');
const cors = require('cors');
const https = require('https');
const fs = require('fs');

const app = express();

app.use(express.json())
app.use(cors());

const PATH = './src/uploads/'
const port = 8443; // Port for server for FILE UPLOADS to run on
let latestColumns = [];
let yColumn = "";
let size = [];
let activations = []
let loss = "";
let hyperparamtersSubmitted = false;
let split = 0.8;
let shape = [0, 1];
let ycsize = [1, 1];
let zScoreVar = false;
let minMaxVar = false;
let oneHotVar = false;
let modelEpochs = 0;
let modelLR = 0;


let uploadStruct = {
    "hasUploaded": false,
    "filePath": ""
}

const storage = multer.diskStorage({
    destination: './src/uploads/',
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
})

const upload = multer({ storage: storage });

app.post('/upload', upload.single('file'), (req, res) => {
    if(req.file) { res.send('hell yeah'); 
        console.log("recieved");
        uploadStruct.hasUploaded = true;
        uploadStruct.filePath = PATH + req.file.originalname
    }
})

app.get('/has-uploaded', (req, res) => {
   res.json(uploadStruct);
});

app.post('/column-selector', (req, res) => {
    let { columns } = req.body;
    latestColumns = columns;
    console.log("recieved columns: ", latestColumns);
    res.send('yes');
});

app.get('/return-column-selector', (req, res) => {
    res.json({'columns': latestColumns});
});

app.post('/select-y-column', (req, res) => {
    let { yColumnName } = req.body;
    yColumn = yColumnName;
    console.log("reciencd: ", yColumnName);
    res.json({'status': 200})
});

app.get('/return-select-y-column', (req, res) => {
    res.json({"yColumnName": yColumn});
});

app.post('/submit-hyperparameters', (req, res) => {
    let { submitted, modelSize, layerActivations, modelLoss, testTrainSplit, dataSetShape, yColumnSize, zScoreVal, minMaxVal, oneHotVal, epochs, lr} = req.body;
    hyperparamtersSubmitted = submitted;
    size = modelSize;
    activations = layerActivations;
    loss = modelLoss;
    split = testTrainSplit;
    shape = dataSetShape;
    ycsize = yColumnSize;
    zScoreVar = zScoreVal;
    minMaxVar = minMaxVal;
    oneHotVar = oneHotVal;
    modelEpochs = epochs;
    modelLR = lr;
});

app.get("/return-hyperparameters", (req, res) => {
    res.json({
        submitted: hyperparamtersSubmitted,
        modelSize: size,
        layerActivations: activations,
        modelLoss: loss,
        testTrainSplit: split,
        dataSetShape: shape,
        yColumnSize: ycsize,
        zScoreVal: zScoreVar,
        minMaxVal: minMaxVar,
        oneHotVal: oneHotVar,
        epochs: modelEpochs,
        lr: modelLR
    });
    console.log(zScoreVar);
})

let accuracyScore = "a";
app.post('/returned-metrics',(req, res) => {
    const { accuracyMetric } = req.body;
    accuracyScore = accuracyMetric;
});

app.get('/get-returned-metrics', (req, res) => {
    res.json({
        accuracyMetric: accuracyScore
    });
});

let lossSubmitted = false;
let lossUrl = "";
app.post("/post-loss-png-url", (req, res) => {
    const { urlSubmitted, pngUrl } = req.body;
    lossUrl = pngUrl;
    lossSubmitted = urlSubmitted;
});

app.get("/get-loss-png-url", (req, res) => {
    res.json({
        submitted: lossSubmitted,
        pngUrl: lossUrl
    });
});

app.listen(port, () => {
    console.log('Server running on port ' + port);
})
