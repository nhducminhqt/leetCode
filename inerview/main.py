from typing import Union, Any
from fastapi import FastAPI, HTTPException
import uvicorn
import jwt
from fastapi import Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer
from inerview.security import validate_token, reusable_oauth2
app = FastAPI(
    title='FastAPI JWT', openapi_url='/openapi.json', docs_url='/docs',
    description='fastapi jwt'
)
SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'
def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt
class LoginRequest(BaseModel):
    username: str
    password: str
def verify_password(username, password):
    if username == 'admin' and password == 'secret':
        return True
    return False
@app.post('/login')
def login(request_data: LoginRequest):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")
@app.get('/data', dependencies=[Depends(validate_token)])
def get_data():
    return {"data": "Secure data"}
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

