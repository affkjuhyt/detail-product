from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = ""
    DB_PORT: str = ""
    DB_USER: str = ""
    DB_PASS: str = ""
    DB_NAME: str = ""
    
    class Config:
        env_file = ".env"
        
SETTINGS = Settings()
