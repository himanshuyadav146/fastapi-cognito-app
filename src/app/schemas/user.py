from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str
    pwd: str

class LoginRequest(BaseModel):
    email: EmailStr
    pwd: str

class ProfileUpdateRequest(BaseModel):
    name: str
    job: str
    job_id: str
    address: str
    organization: str