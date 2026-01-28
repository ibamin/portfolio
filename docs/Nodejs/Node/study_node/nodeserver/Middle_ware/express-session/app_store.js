const express =require('express');
const session = require('express-session');
const fileStore = require('session-file-store')(session);
const bodyparser = require('body-parser');
const app = express();
const port =3000;

const sessionDir = './sessions';
const fs = require('fs');

if(!fs.existsSync(sessionDir)){
    fs.mkdirSync(sessionDir);
}

app.use(session({
    secret:"secret key",
    resave: false,
    saveUninitialized: true,
    cookie:{
        httpOnly:true,
        secure:false,
        maxAge:60000
    },
    store: new fileStore({
        path:sessionDir,
        logFn: function(){}
    })
}));

function checkSession(req,res,next){
    if(req.session && req.session.is_logined){
        next();
    }else{
        res.redirect('/login');
    }
}

app.use(bodyparser.json());

app.get('/',function(req,res){
    console.log(req.session);
    res.send(req.session);
});

app.get('/login',function(req,res){
    res.send('login page');
});

app.post('/login',function(req,res){
    const {email,pw} = req.body;
    req.session.email=email;
    req.session.is_logined=true;
    req.session.save(err=>{
        if(err) throw err;
        res.redirect('/home');
    });
});

app.post('/logout',checkSession,(req,res,next)=>{
    req.session.destroy();
    res.redirect('/login');
});

app.get("/home",function(req,res){
    res.send("this place home");
});

app.listen(3000,()=>{
    console.log(`start server port: ${port}`);
});