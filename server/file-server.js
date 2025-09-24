const express = require('express');
const multer = require('multer');
const cors = require('cors');
const https = require('https');
const fs = require('fs');

const app = express();

app.use(express.json())
app.use(cors());

const PATH = './uploads/'
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



let uploadStruct = {
    "hasUploaded": false,
    "filePath": ""
}

const storage = multer.diskStorage({
    destination: './uploads/',
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
    let { submitted, modelSize, layerActivations, modelLoss, testTrainSplit, dataSetShape, yColumnSize } = req.body;
    hyperparamtersSubmitted = submitted;
    size = modelSize;
    activations = layerActivations;
    loss = modelLoss;
    split = testTrainSplit;
    shape = dataSetShape;
    ycsize = yColumnSize;
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
    });
})

/*
const privateKey = fs.readFileSync('/etc/ssl/name_com/PRIVATEKEY.key', 'utf8');
const certificate = fs.readFileSync('/etc/ssl/name_com/2507935545.crt', 'utf8');
const bundle = fs.readFileSync('/etc/ssl/name_com/bundle.crt', 'utf8');
const passphrase = fs.readFileSync('/etc/ssl/name_com/PASSPHRASE.txt', 'utf8').slice(0, 11);

const credentials = {
	key: privateKey,
	cert: certificate,
	ca: bundle,
	passphrase: passphrase
};


https.createServer(credentials, app).listen(port, () => {
    console.log('Server Running on port ' + port);
});
*/

app.listen(port, () => {
    console.log('Server running on port ' + port);
})
