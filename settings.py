# settings.py

"""
class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        if value not in {"dev", "test", "prod"}:
            raise ValueError
       ... # implement me!
       # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
       return value
"""
