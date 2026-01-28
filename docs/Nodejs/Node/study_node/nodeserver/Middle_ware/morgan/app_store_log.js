const express = require('express');
const morgan  = require('morgan');
const fs = require('fs');
const path = require('path');

const app = express();

const accessLogStream = fs.createWriteStream(path.join(__dirname,'access.log'),{
    flag : 'a'
});

app.use(morgan('combined',{stream:accessLogStream}));

app.get('/',function(req,res){
    res.send('hello world');
});

app.listen(3000,()=>{
    console.log(`serve start port 3000`);
});