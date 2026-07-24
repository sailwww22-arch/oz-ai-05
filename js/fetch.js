//fetch api
//get 요청
fetch("https://jsonplaceholder.typicode.com/posts")
     .then (Response => Response.json()) // 응답 메세지에서 json 데이터 추출
     .then (data => console.log(data)) // 콘솔에 출력


//post 요청
// post 요청
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: "python", body: "hello, python" })
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));