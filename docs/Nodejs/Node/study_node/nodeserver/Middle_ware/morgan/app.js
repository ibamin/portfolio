const express = require('express');
const morgan = require('morgan');

const app = express();

app.use(morgan('combined'))

app.get('/',function(req,res){
    res.send('hello, world');
});

app.listen(3000,()=>{
    console.log(`server start port : 3000`);
});