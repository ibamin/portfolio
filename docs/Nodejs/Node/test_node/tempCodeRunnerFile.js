const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"]
  }
});
var server_start_time = Date.now();
const port = 3000;
const now = new Date();
const month = now.getMonth() + 1;
const year = now.getFullYear();
const fileName = `${year}-${month}.txt`;
const filePath = path.join(__dirname, fileName);
const flag = fs.existsSync(filePath) ? 'a' : 'ax';
fs.writeFileSync(filePath, '', { flag });
var currentData = {};

app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
  console.log('A user connected');

  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });

  socket.on('data', (text) => {
    const [ip,port] = text.split(',');
    
    if ([ip,port] in currentData) {
      currentData[ip,port]++;
      if(currentData[ip]>10 && Date.now()-server_start_time>=300000){
        io.emit(currentData[ip]);
        server_start_time=Date.now();
      }
    } else {
      currentData[ip,port]=1;
    }
    console.log(currentData);
    fs.writeFileSync(filePath,text,flag);
  });
});

http.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
  console.log(`server-time :${server_start_time}`);
});
