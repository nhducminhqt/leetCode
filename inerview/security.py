from datetime import datetime
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

reusable_oauth2 = HTTPBearer(scheme_name='Authorization')

def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    try:
        payload = jwt.decode(
            http_authorization_credentials.credentials, 
            SECRET_KEY, 
            algorithms=[SECURITY_ALGORITHM]
        )
        
        expiration_time = payload.get('exp')
        
        if expiration_time and datetime.utcfromtimestamp(expiration_time) < datetime.utcnow():
            raise HTTPException(status_code=403, detail="Token expired")
        
        return payload.get('username')

    except jwt.PyJWTError:  
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials"
        )
