const fs = require('fs');
const {Console} = require('console');

const output = fs.createWriteStream('./stdout.log');
const erroroutput = fs.createWriteStream('./stderr.log');

const logger = new Console({stdout:output,stderr:erroroutput});
let count=0;
process.argv.forEach(function(val,index,array){
    count = val;
})
logger.log(`count : ${count}`);
logger.error(`count: ${count}`);

fs.readFile('./stdout.log','utf-8',(err,data)=>{
    if(err) throw err;
    console.log(data);
});

var text= fs.readFileSync('./stdout.log','utf8');
console.log(text);

let data = '파일 쓰기 테스트';
fs.writeFile("./stdout.log",data,'utf8',(err)=>{
    if(err) throw err;
    console.log("async file wirte");
});

fs.writeFileSync("./stdout.log",data,'utf8');
console.log("Sync file write");
