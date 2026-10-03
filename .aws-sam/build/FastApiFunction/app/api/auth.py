from fastapi import APIRouter, HTTPException, status
from app.schemas.user import RegisterRequest, LoginRequest
from app.services.cognito_service import CognitoService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(req: RegisterRequest):
    try:
        res = CognitoService.sign_up(req.email, req.pwd, req.name, req.phone)
        return {"message": "User registered successfully", "userSub": res["UserSub"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(req: LoginRequest):
    try:
        res = CognitoService.login(req.email, req.pwd)
        auth_data = res.get("AuthenticationResult", {})
        return {
            "access_token": auth_data.get("AccessToken"),
            "id_token": auth_data.get("IdToken"),
            "refresh_token": auth_data.get("RefreshToken"),
            "expires_in": auth_data.get("ExpiresIn"),
            "token_type": "Bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))