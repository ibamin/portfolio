const express = require('express');
const responseTime = require('response-time');

const app = express();

app.use(responseTime((req,res,time)=>{
    console.log(`${req.method} ${req.url} ${time}`);
}));

app.get('/',function(req,res){
    res.send('hello, world');
});

app.listen(8080);