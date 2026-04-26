const express =require('express');
const session = require('express-session');
const app = express();

app.use(session({
    secret:'secret key', //암호화하는 데 쓰일 키
    resave: false, //세션에 변경 사항이 없어도 항상 다시 저장할지 여부
    saveUninitialized: true, //초기화되지 않은 세션을 스토어에 강제로 저장할지 여부
    cookie:{//세션 관리 쿠키
        httpOnly:true, //true면 클라이언트 자바 스크립트에서 document.cookie로 쿠키 정보를 볼 수 없음
        secure:true, //true면 https에서만 쿠키 정보를 주고 받도록 처리
        maxAge:60000 //쿠키가 유지되는 시간 (밀리세컨드 단위)
    }
}));

app.get('/',function(req,res){
    res.send("default session use");
})

app.listen(3000,()=>{
    console.log("3000번 포트로 실행했습니다.");
});