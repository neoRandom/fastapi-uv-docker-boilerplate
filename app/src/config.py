from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from os import path as ospath

def get_password(path):
    if ospath.exists(path):
        with open(path, 'r') as f:
            return f.read().strip()
    return ""


class Settings(BaseSettings):
    # Variáveis vindas do compose.yaml
    POSTGRES_HOST: str = "" 
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD_FILE: str = ""
    REDIS_HOST: str = ""
    REDIS_PORT: int = 6379

    @computed_field
    @property
    def POSTGRES_URL(self) -> str:
        # Lógica para ler a senha do arquivo (Docker Secrets)
        password = get_password(self.POSTGRES_PASSWORD_FILE)
        url = f"postgresql+psycopg://{self.POSTGRES_USER}:{password}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        # url = f"postgresql+psycopg://postgres@database:5432/project_db"

        return url

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
