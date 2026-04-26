const express = require("express");
const app = express();
const port = 3000;

app.listen(3000,()=>{
    console.log(`server start port:${port}`);
});

app.get('/error',function(req,res){
    throw new Error("active error");
});

app.get('/error2',function(req,res,next){
    next(new Error('active error2'));
});

app.use(function(err,req,res,next){
    res.status(500).json({statusCode:res.statusCode,errMassage:err.message});
});
