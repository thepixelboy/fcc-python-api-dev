from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_pass: str
    db_name: str
    db_user: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
