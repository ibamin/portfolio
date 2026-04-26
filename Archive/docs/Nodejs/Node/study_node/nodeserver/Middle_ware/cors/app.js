const express =require('express');
const cors =require('cors');
const app = express();

const corsOption={
    origin:"http://example.com",
    optionSuccessStatus:200
};

app.use(cors(corsOption));

app.get('/products',function(req,res,next){
    res.json({mes:"this is cors-enabled for all origins!"});
});

app.listen(3000,()=>{
    console.log(`server start port 3000`);
});