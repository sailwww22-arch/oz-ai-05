// 할 일을 입력하고 추가 버튼을 누르면
// 할 일 목록에 할 일이 추가되어야 함
const todoInput = document.querySelector("#todo-input")
const addBtn = document.querySelector("#add-btn")
const todoList = document.querySelector("#todo-list")
let todos = []
// 미리 저장된 todos가 있는지 확인
const savedtodos = JSON.parse(localStorage.getItem("todos")) || []

todos = savedtodos

for (const t of todos) {
    rendertodo(t)
}
// 전체 todo 를 화면에 그리는 함수
function rendertodo(todo) {
    const li = document.createElement("li")
    li.className = "list-group-item d-flex justify-content-between align-items-center"
    li.textContent = todo

    const btn = document.createElement("button")
    btn.className = "btn btn-sm btn-danger"
    btn.textContent = "삭제"
    btn.addEventListener("click", () => {
        const index = todos.indexOf(todo)
        if (index === -1) return
        todos.splice(index, 1)
        localStorage.setItem("todos", JSON.stringify(todos))
        todoList.removeChild(li)
    })
    li.appendChild(btn)
    todoList.appendChild(li)
}
// 할일 추가
addBtn.addEventListener("click", () => {
    const todo = todoInput.value.trim()
    if (todo === "") {
        alert("할 일을 입력하세요.")
        return
    }

    todos.push(todo)
    localStorage.setItem("todos", JSON.stringify(todos))
    rendertodo(todo)
    todoInput.value = ""
})

