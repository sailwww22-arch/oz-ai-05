function add(n1, n2) {
      return n1 + n2

}

// 함수를 호출
console.log(add(10,  5))
function sayhello() {
     console.log("hello");


}
// 함수 호출 -> 호출
let result = sayhello()
console.log(result);

let resut = sayhello
console.log(result);


//result => 함수
//result => undefined

function run(fn) {
    // sayhello 호출
    fn() // undefined


}
run(1)
function sayhello() {
    console.log("hello")
    //return undefined

}
run(sayhello) //undefined
//run 함수 호출
