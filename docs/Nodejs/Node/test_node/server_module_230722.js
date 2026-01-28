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
var classData = [];
var Attackcount = {
  "BENIGN": 1,
  "DoS Hulk": 1,
  "DoS Slowhttptest": 1,
  "FTP-Patator": 1,
  "SSH-Patator": 1,
}

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
  console.log('A user connected');

  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });

  socket.on('data', (text) => {
    const [lineNumber, percentage, className, dataList] = text;
    if (className in currentData) {
      for (let i = 0; i < currentData[className].length; i++) {
        currentData[className][i] = (currentData[className][i] + dataList[i + 1]) / 2;
      }
    } else {
      currentData[className] = dataList.slice(1);
    }
    Attackcount[className]++;
    console.log(currentData);
    const textData = JSON.stringify(currentData) + '\n';
    fs.writeFileSync(filePath,textData,{flag});
    io.emit('message', textData);
  });
});

http.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
