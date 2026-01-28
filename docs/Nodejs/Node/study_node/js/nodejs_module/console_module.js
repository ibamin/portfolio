console.log('hello world');
console.log('hello %s',"word");

const world ='world';
console.log(`hello ${world}`);

console.error(new Error('에러 메시지 출력'));

const arr=[
    {name:'John Doe',email : 'john@mail.com'},
    {name:'Jeremy Go',email:'jeremy@mail.com'}
];
console.table(arr);

const obj={
    student:{
        gradel1:{class1:{},class2:{}},
        gradel2:{class1:{},class2:{}},
        teacher:['John Doe','Jeremy Go']
    }
};

console.dir(obj,{depth:1,colors:true});

console.time('time for for-loop');
for(let i=0; i<999999;i++){}
console.timeEnd('time for for-loop');