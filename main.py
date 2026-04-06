import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    config_dir = "config"

    env = os.path.join(config_dir, f".env.{environment}")
    if not os.path.exists(env):
        raise FileNotFoundError(f"{env} nie istnieje")
    load_dotenv(dotenv_path=env, override=True)

    if os.path.exists("secrets.yaml"):
        with open("secrets.yaml", "r") as f:
            for key, value in yaml.safe_load(f).items():
                os.environ[key] = str(value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables from specified.env file.")
    parser.add_argument("--environment", type=str, default="dev", help="The environment to load (dev, test, prod)")
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET: ", settings.SECRETS)