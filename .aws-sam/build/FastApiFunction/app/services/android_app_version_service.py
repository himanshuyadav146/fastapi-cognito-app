import boto3

from app.core.config import settings

dynamodb = boto3.resource("dynamodb", region_name=settings.AWS_REGION)
table = dynamodb.Table(settings.ANDROID_APP_VERSION_TABLE)


class AndroidAppVersionService:
    @staticmethod
    def update_current_version(version: str) -> str:
        response = table.update_item(
            Key={"platform": "android"},
            UpdateExpression="SET #version = :version",
            ExpressionAttributeNames={"#version": "version"},
            ExpressionAttributeValues={":version": version},
            ReturnValues="UPDATED_NEW",
        )
        return response["Attributes"]["version"]

    @staticmethod
    def get_current_version() -> str | None:
        response = table.get_item(Key={"platform": "android"})
        item = response.get("Item")
        if item is None:
            return None

        return item["version"]
