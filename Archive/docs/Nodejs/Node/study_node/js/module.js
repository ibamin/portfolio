const {add,minus,mul,divide} = require("./calculator");
let argv=[];
 process.argv.forEach(function(val,index,array){
    argv.push(val);
 })

console.log(`about : ${argv[0]}`)
console.log(`exe File path : ${argv[1]}`)
console.log(`a:${argv[2]}`)
console.log(`b:${argv[3]}`)

console.log(add(argv[2],argv[3]));
console.log(minus(argv[2],argv[3]));
console.log(mul(argv[2],argv[3]));
console.log(divide(argv[2],argv[3]));
