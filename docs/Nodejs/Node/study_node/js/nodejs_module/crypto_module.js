const crypto =require('crypto');
let log_cryp=crypto.createHash('sha512').update('pw1234').digest('base64');
console.log(log_cryp);
log_cryp = crypto.createHash('sha512').update('pw1234').digest('hex');
console.log(log_cryp);
log_cryp = crypto.createHash('sha512').update('pw1234').digest('decimal');


let salt="";

const createsalt=()=>{
    return new Promise((resolve,reject)=>{
        crypto.randomBytes(64,(err,buf)=>{
            if(err) reject(err);
            resolve(buf.toString("base64"));
        });
    })
};

const createCryptoPassword = async (plainPassword)=>{
    salt = await createsalt();

    return new Promise((resolve,reject)=>{
        crypto.pbkdf2(plainPassword,salt,100000,64,"sha512",(err,key)=>{
            if(err) reject(err);
            resolve({password:key.toString("base64"),salt});
        });
    })
};

const getCryptoPassword = (plainPassword,salt)=>{
    return new Promise((resolve,reject)=>{
        crypto.pbkdf2(plainPassword,salt,9999,64,"sha512",(err,key)=>{
            if(err) reject(err);
            resolve({password:key.toString("base64"),salt});
        });
    })
};

let argv=[];
 process.argv.forEach(function(val,index,array){
    argv.push(val);
 })
 if (argv[2]) {
    createCryptoPassword(argv[2])
        .then((result) => {
            console.log("생성된 암호:", result);
        })
        .catch((error) => {
            console.error("암호 생성 오류:", error);
        });

    getCryptoPassword(argv[2], salt)
        .then((result) => {
            console.log("응답:", result);
        })
        .catch((error) => {
            console.error("오류:", error);
        });
} else {
    console.log("사용법: node your-script.js [password]");
}