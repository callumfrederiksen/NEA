const express = require('express');
const multer = require('multer');
const cors = require('cors');

const app = express();
app.use(cors());

const storage = multer.diskStorage({
    destination: './',
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
})

const upload = multer({ storage: storage });



app.post('/upload', upload.single('file'), (req, res) => {
    if(req.file) { res.send('hell yeah'); }
})

app.listen(3001, () => {
    console.log('server ruuning');
})