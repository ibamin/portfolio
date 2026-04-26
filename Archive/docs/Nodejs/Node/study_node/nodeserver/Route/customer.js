const express = require('express');
const router = express.Router();

router.get('/',function(req,res){
    res.send("customer root");
});

router.get('/insert',function(req,res){
    res.send("/customer/insert");
});

router.get('/update',function(req,res){
    res.send("/customer/update");
});

router.get('/delete',function(req,res){
    res.send("/customer/delete");
});

module.exports=router;