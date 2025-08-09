const port = 8443; // Port for server for FILE UPLOADS to run on 
let latestColumns = [];

const express = require('express');
const multer = require('multer');
const cors = require('cors');
const https = require('https');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json())

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

}
})

app.post('/column-selector', (req, res) => {
    let { columns } = req.body;
    latestColumns = columns;
    console.log("recieved columns: ", latestColumns);
    res.send('yes');
});

app.get('/return-column-selector', (req, res) => {
    res.json({'columns': latestColumns});
});

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


// app.listen(port, () => {
//     console.log('Server running on port ' + port);
// })
