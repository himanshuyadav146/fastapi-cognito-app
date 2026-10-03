import boto3
from app.core.config import settings

dynamodb = boto3.resource("dynamodb", region_name=settings.AWS_REGION)
table = dynamodb.Table(settings.DYNAMODB_TABLE)

class DynamoDBService:
    @staticmethod
    def save_user_profile(user_id: str, profile_data: dict):
        item = {"userId": user_id, **profile_data}
        table.put_item(Item=item)
        return item