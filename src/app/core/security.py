from fastapi import Header, HTTPException, status
from typing import Optional
from app.services.cognito_service import CognitoService

async def get_current_user_id(authorization: Optional[str] = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing ya format galat hai (Bearer <token>)"
        )
    
    token = authorization.split(" ")[1]
    try:
        user_info = CognitoService.get_user_from_token(token)
        sub = next(attr["Value"] for attr in user_info["UserAttributes"] if attr["Name"] == "sub")
        return sub
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token verification fail ho gaya: {str(e)}"
        )