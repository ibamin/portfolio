fetch("http://localhost:3000/comments")
.then((response)=>response.json())
.then((json)=>console.log(json));

fetch("http://localhost:3000/comments/1")
.then((response)=>response.json())
.then((json)=>console.log(json));

fetch("http://localhost:3000/comments?postId=1")
.then((response)=>response.json())
.then((json)=>console.log(json));