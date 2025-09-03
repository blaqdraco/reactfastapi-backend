from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str = ""
    ALLOWED_ORIGINS: List[str] = []   # should be a list, not a str
    OPENAI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v: str | List[str]) -> List[str]:
        if isinstance(v, str):
            return v.split(",") if v else []
        return v

    class Config:   # ✅ must be "Config", not "config"
        env_file = ".env"
        env_file_encoding = "utf-8"   # typo fixed: was env_file_coding
        case_sensitive = True         # typo fixed: was case_senstive


settings = Settings()  # ✅ fixed: was `settings = settings ()`
