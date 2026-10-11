from pydantic import BaseModel, Field, field_validator


class AndroidAppVersionUpdateRequest(BaseModel):
    version: str = Field(min_length=1, max_length=50)

    @field_validator("version", mode="before")
    @classmethod
    def strip_version(cls, value: str) -> str:
        if isinstance(value, str):
            value = value.strip()
        return value
