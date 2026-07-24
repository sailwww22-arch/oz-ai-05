from 
from schema import UserSignupreqest, Userresponse

app = fastapi.FastAPI(), fastapi.Path

users = list[dict[str, int | str]] = [
    {"id": 1, "name": "alex", "password": "1234"},
    {"id": 2, "name": "bob", "password": "1234"},
    {"id": 3, "name": "chris", "password": "1234"},
]

@app.get("/users", 
         summary="전체 사용자 조회 API",
         response_model=list[Userresponse],
         status_code = 200 #응답이 성공한 경우, 사용할 상태코드 값 지정
         )
def get_users():
    return users
   

# 1) 행위(action) -> http method (get, post, put/patch, delete)
# 2) 대상(resource) -> url( = uniform resource locator)

@app.get("/hello")
def hello():
    return {"msg": "hello"}

# 클아이너트가 /hi 로 get 요청을 했을때, "hi"가 출력되게 
@app.get("/hi")
def hi():
    return {"msg": "hi"}
#[실습]
# get/ users / 10 요청했을때, {"id": 10 "name": "david"} 응답
@app.get("/users/10")
def get_user_10():
    return {"id": 10, "name": "david"}
@app.get(
    "/users/{user_id}", 
    summary="회원 조회 API", 
    response_model = Userresponse,
    status_code = 200
    )
def get_user(user_id: int = fastapi.Path(..., ge=1)):
    for user in users:
        if user_id ==user["id"]:
            return user
   #user_id에 해당하는 user 가 없는경우
   raise HTTPexception(
       status_code=404,
       
   )

#ge = 이상

# 특정 경로로 값이 바뀌는 경우 path parameter로 처리 
# 예) users/(user_id)
# a) 함수에 path parameter 값을 전달
# def get_user(iser_id):
# b) path parameter 값에 타입을 제한 -> type hints
# def get_user(user_id:link):
# c) 타입이 잘못된 경우 : 422에러


#[실습]
# 1) item_name을 str 타입으로 고정
# 2) item_name의 최대 글자수(max_length)를 6글자로 고정
@app.get("/items/{item_name}")
def get_item(item_name: str = fastapi.Path(..., max_length=6)):
    return {"item_name": item_name}

#path 사용하는것은 path 경로 상에서 찾아와라라는 뜻
# query parameter
# get google.com/search?q=python

# get /users/search?name=alex
@app.get(
    "/users/search", 
    summary="회원 검색 API", 
    response_model=list[Userresponse],
    status_code = 200
    )
def search_user(name: str | None = fastapi.Query(None)):  # -> 검색어가 비어있다는 뜻
    # def search_user (name: str = path(..., min_length=2)): 라고 쓰면 -> path 상에서 찾아와라라는뜻
   result = []
   if name is None:
       return result
   
   for user in users:
       if name in user["name"]:
           result.append(user)
   
   return result
# 경로상 따로 이름을 정해 주지 않으면 query parameter 로 먼저 찾아옴
# if => get /users/search? => 이름이 없으므로 에러

#[실습]
#1) q: str, limit: int 두개의 쿼리 파라미터 받기
#2) q: 필수 limit: 필수아님 (기본:10)
@app.get("/items/search")
def search_item_handler(q: str = fastapi.Query(...) ,limit: int = fastapi.Query(10)):
    return {"q": q, "limit": limit}


#type Hints
# 변수 함수 데이터의 의도된 타입을 코드로 명시하는 문법
# 코드 가독성 향상, IDE 자동완성 & 오류 사전 탐지, 런타임 검증 도구, FastApi의 핵심동작 Type hints 위애 설계되어 있음
# 강제성이 없음 
# 기본 type hints 문법 
# 1) : 뒤에 타입 지정
# 2) 실행자체에는 영향 없음 (순수 python문법)

# pydantic
# 데이터 검증 + 파싱을 담당하는 라이브러리
# 1) pydantic은 데이터의 유효성(형식, 제약조건)을 검사하는 라이브러리
# 2) 간닩한 문법으로 데이터의 


@app.post(
    "/users",
    summary = "회원 생성 API",
    response_model = Userresponse
)
def user_sign_up_handler(
    body: UserSignupreqest
):
    new_user = {
        "id": 100,
        "name": body.name,
        "password": body.password
    }

    return new_user 
