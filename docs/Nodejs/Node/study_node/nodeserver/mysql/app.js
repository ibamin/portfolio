const express = require('express');
require('dotenv').config({path:'./.env'});
const mysql = require('./index');

const app = express();

app.use(express.json({
    limit:'50mb'
}));

app.listen(3000,()=>{
    console.log("server start port 3000");
});

app.get("/api/customers",async (req,res)=>{
    const customers =await mysql.query('customerList');
    console.log(customers);
    res.send(customers);
})

app.post('/api/customers/insert',async (req,res)=>{
    const customer =await mysql.query('customerInsert',req.body.param);
    console.log(customer);
    res.send(customer);
})

app.put('/api/customers/update',async (req,res)=>{
    const customer = await mysql.query('customerupdate',req.body.param);
    console.log(customer);
    res.send(customer);
})

app.delete('/api/cusomers/delete/:id',async (req,res)=>{
    const {id} = req.params;
    const customer = await mysql.query('customerdelete',id);
    res.send(customer);
})