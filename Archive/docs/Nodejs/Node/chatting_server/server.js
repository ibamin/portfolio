const express = require('express');
const { response } =require('express');
const path = require('path');
const fs = require('fs');
const nunjucks =require('nunjucks');   //랜더링 필수 패키지
const app = express();
const http = require('http').Server(app);
const  io = require('socket.io')(http);

app.set("view engine","html")

nunjucks.configure("./views",{
    express: app
});

app.use('/',express.static("./public"));                  

app.get('/',(req,res)=>{
    res.render("main.html");
});

var people_cnt = 0;                                   
io.on('connection',function(socket){                             //http와 node js가 가지고있는 핸들러를 socket으로 이관
    console.log('user connected : ',socket.id);   
    people_cnt++;

    socket.on('disconnect',function(){                          //접속 해제
        console.log('user disconnected : ',socket.id);
    });

    socket.on('send message',function(text){                     //메시지 전송
        var date = new Date;
        var message =  text + '\n' + date;
        console.log(message);
        io.emit('receive message',message);                    //receive message이벤트임을 클라이언트에게 message와 함께 전송
    });
});

http.listen(3000,function(req,res){                           //서버와 오픈
    console.log('server running~~ port : 3000');
});