import re 
from pydantic import BaseModel, Field, field_validator



# 회원 가입 요청에 사용되는 데이터 형식
class usersignuprequest(BaseModel):
    name: str = Field(..., min_length= 2)   #최소 2글자 이상
    password: str = Field(..., min_length=4, max_length=10 ) #최소 4글자이상
    
    @field_validator
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("대문자가 최소 1개 이상 포함되어야 합니다.")
        if not re.search(r"[a-z]", value):
            raise ValueError("소문자가 최소 1개 이상 포함되어야 합니다.")
        return
# 사용자 데이터를 응답할 때 사용되는 데이터 형식
class userresponse(BaseModel):
    id: int
    name: str
   
