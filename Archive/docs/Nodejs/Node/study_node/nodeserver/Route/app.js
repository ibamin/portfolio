const express = require('express');
const app = express();
const customer = require("./customer");
const product = require("./product");
const port = 3000;

app.use(express.json({
    limit:'50mb'
}));

app.listen(port,()=>{
    console.log(`Server started. port:${port}`);
});

app.use('/customer',customer);
app.use('/product',product);