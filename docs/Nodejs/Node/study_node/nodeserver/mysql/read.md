sql.js에 sql추가
index.js는 mysql에 연결하는 pool구조 제작
app.js 는 서버 구축

npm install --svae-dev nodemon 으로 모듈을 설치후

node 대신 nodemon을 통해 js파일을 실행시 파일이 존재하는 디렉토리에 변화가 있으면
수동 재시작이 아닌 자동으로 재시작이 된다

특정 디렉토리만 감시하고자하면
nodemon --watch [감시대상] [재실행파일]
ex)
nodemon --watch mysql app.js
