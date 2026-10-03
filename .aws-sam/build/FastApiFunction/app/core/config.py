import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    USER_POOL_ID: str = os.getenv("USER_POOL_ID", "us-east-1_vNlxDGXqN")
    CLIENT_ID: str = os.getenv("CLIENT_ID", "1haf1t8lc17amggpvpc3an3cve")
    DYNAMODB_TABLE: str = os.getenv("DYNAMODB_TABLE", "UserProfiles")

settings = Settings()





