import boto3
from app.core.config import settings

cognito_client = boto3.client("cognito-idp", region_name=settings.AWS_REGION)

class CognitoService:
    @staticmethod
    def sign_up(email: str, password: str, name: str, phone: str):
        return cognito_client.sign_up(
            ClientId=settings.CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[
                {"Name": "email", "Value": email},
                {"Name": "name", "Value": name},
                {"Name": "phone_number", "Value": phone}
            ]
        )

    @staticmethod
    def login(email: str, password: str):
        return cognito_client.initiate_auth(
            ClientId=settings.CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": email, "PASSWORD": password}
        )

    @staticmethod
    def get_user_from_token(token: str):
        return cognito_client.get_user(AccessToken=token)