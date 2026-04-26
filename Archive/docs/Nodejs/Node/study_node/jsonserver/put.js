fetch("http://localhost:3000/posts/3",{
    method:"PUT",
    body:JSON.stringify({
        id:2,
        title:"The Grate Jeremy",
        author: "Jeremy",
    }),
    headers:{
        "content-type":"application/json; charset=UTF-8",
    },
})
.then((response)=>response.json())
.then((json)=>console.log(json));