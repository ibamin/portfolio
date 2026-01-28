const express = require('express');
const router = express.Router();

router.get('/',function(req,res){
    res.send("product root");
});

router.get('/insert',function(req,res){
    res.send("/product/insert");
});

router.get('/update',function(req,res){
    res.send("/product/update");
});

router.get("/delete",function(req,res){
    res.send("/product/delete");
});

module.exports=router;