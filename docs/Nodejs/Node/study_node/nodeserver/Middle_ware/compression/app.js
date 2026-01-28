const compression=require('compression');
const express = require('express');

const app = express();

app.use(compression());
//특별한 path만 압축할때
app.use('/api/getMap',compression())