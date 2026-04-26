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
    console.log(text.ip);
    const ip=text.ip;
    console.log(text.port);
    const port = text.port;
    const key = `${ip},${port}`;
  if (currentData.hasOwnProperty(key)) {
    currentData[key]++;
  } else {
      currentData[key]=1;
      console.log("new data");
      console.log("ip="+ip);
      console.log("port="+port);
    }
    console.log(currentData[key]);
    const fileInput = `ip=${ip}  port=${port}  Time=${Date.now()}\n`;
    fs.writeFileSync(filePath,fileInput, { encoding: 'utf-8', flag });
  });
});

setInterval(() => {
  Object.entries(currentData).forEach(([key, value]) => {
    const [ip, port] = key.split(',');
    if (value >= 10) {
      io.emit('sudden_attack', { ip, port, count: value });
    }
  });
}, 300000);

http.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
  console.log(`server-time :${server_start_time}`);
});
