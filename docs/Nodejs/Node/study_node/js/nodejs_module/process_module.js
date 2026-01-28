const process = require('process');

process.on('beforeExit',(code)=>{
    console.log('2. 이벤트 루프에 등록된 작업이 모두 종료된 후 노드 프로세스를 종료하기 직전 :',code);
});

process.on('exit',(code)=>{
    console.log('3.노드 프로세스가 종료될 때 : ',code);
});

console.log('1. printing message on console to first');

console.log(process.env);

const {nextTick} = require('process');

console.log('start');

setTimeout(()=>{
    console.log("timeout callback");
},0);

nextTick(()=>{
    console.log('nextTick callback');
});
console.log('end');