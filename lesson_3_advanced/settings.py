from typing import Optional


from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = "api/v1"
    MONGODB_URL: HttpUrl
    GF_API_URL: Optional[str] = None
    TOKEN_SECRET_KEY: str = "fj0823t8y3t9shoidn9184h13iudhaslidfuh3190841-00=52394hfu"


settings = Settings()

print(settings.MONGODB_URL)
