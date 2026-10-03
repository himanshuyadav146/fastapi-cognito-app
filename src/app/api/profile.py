from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import ProfileUpdateRequest
from app.core.security import get_current_user_id
from app.services.dynamodb_service import DynamoDBService

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.post("/update")
def update_profile(
    req: ProfileUpdateRequest,
    user_id: str = Depends(get_current_user_id)
):
    try:
        saved_item = DynamoDBService.save_user_profile(user_id, req.model_dump())
        return {"message": "Profile updated successfully", "data": saved_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))