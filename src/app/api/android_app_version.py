import logging

from fastapi import APIRouter, HTTPException, status
from botocore.exceptions import BotoCoreError, ClientError

from app.schemas.android_app_version import AndroidAppVersionUpdateRequest
from app.services.android_app_version_service import AndroidAppVersionService

router = APIRouter(prefix="/android-app", tags=["Android App"])
logger = logging.getLogger(__name__)


@router.post("/version")
def update_android_app_version(req: AndroidAppVersionUpdateRequest):
    try:
        version = AndroidAppVersionService.update_current_version(req.version)
    except (BotoCoreError, ClientError) as error:
        logger.exception("Failed to update Android app version")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "message": "Failed to update Android app version.",
            },
        ) from error

    return {
        "success": True,
        "message": "Android app version updated successfully.",
        "version": version,
    }


@router.get("/version")
def get_android_app_version():
    version = AndroidAppVersionService.get_current_version()
    if version is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Android app version has not been configured.",
        )

    return {"platform": "android", "version": version}
