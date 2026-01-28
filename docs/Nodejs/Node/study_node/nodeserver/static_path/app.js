const express = require('express');
const app = express();
const port =3000;

app.listen(3000,()=>{
    console.log(`start server port :${port}`);
});

/***
 * public의 모든 파일들을 url로 제공가능
 */
app.use(express.static('public'));
