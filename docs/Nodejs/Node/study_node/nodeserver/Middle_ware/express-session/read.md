npm install express-session
app_default.js

세션을 관리하기위한 미들웨어 cookie-session과는 다르게
데이터를 서버에 저장하기 때문에 쿠키보다 더 안전하고 더 많은 데이터를
저장가능

npm install session-file-store
app_store.js

세션정보를 파일로 저장해서 관리가능
req.session.destory(); 부분에서
[session-file-store] will retry, error on last attempt: Error: ENOENT: no such file or directory, open 'C:\java\Nodejs\Node\study_node\nodeserver\Middle_ware\express-session\sessions\PRmtBVEIrSUGDsDGq--LDPErfcb2ysCP.json'
와 같은 오류들이 일어났는데

이유는 session-file-store가 express-session의 일부라서 express-session이 세션파일을 찾을 수 없을 때 새파일을 만들기 때문에 주요 문제는 아니다

해결 방안
session-file-store의
filestore옵션에
logFn: function(){} 을 추가한다
