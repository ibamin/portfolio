const timeout = setTimeout(()=>{
    console.log("1초 후에 실행됩니다");
},1000);

const interval = setInterval(() => {
   console.log("1초 마다 실행됩니다"); 
}, 1000);

const immediate = setImmediate(()=>{
    console.log('setImmediate() 함수 호출 뒤에 오는 모든 코드를 먼저 실행하고 바로 다음에 실행합니다')
});

console.log('setImmediate 보다 먼저 실행됩니다.');

setTimeout(()=>{
    clearInterval(interval);
},3000);