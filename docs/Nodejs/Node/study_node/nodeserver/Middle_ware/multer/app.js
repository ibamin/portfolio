const multer = require('multer')
const express = require('express');
const path = require('path');
const app = express();

app.use(express.json({
    limit:'50mb'
}));

app.listen(3000,()=>{
    console.log('server start port:3000');
});

const storage = multer.diskStorage({
    destination:function(req,file,cb){
        cb(null,'uploads/');
    },
    filename: function(req,file,cb){
        cb(null,new Date().valueOf()+path.extname(file.originalname));
    }
});

const upload=multer({storage:storage});

app.get('/',function(req,res){
    res.sendFile(__dirname+"/multer.html");
});

app.post('/profile',upload.single('avatar'),function(req,res,next){
    console.log(req.file);
    console.log(req.body);
});

app.post('/photos/upload',upload.array('photos',12),function(req,res,next){
    console.log(req.file);
});