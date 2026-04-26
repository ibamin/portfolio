const defalutNum=1;

function add(num1,num2){
    return num1+num2;
}

function minus(num1,num2){
    return num1>num2 ? num1-num2:num2-num1;
}

function mul(num1,num2){
    return num1*num2;
}

function divide(num1,num2){
    return num1/num2;
}

module.exports={
    add,minus,mul,divide
}