import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(key: str):
    secret_path = BASE_DIR / "secrets.json"

    with open(secret_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        raise EnvironmentError(f"Set the {key} environment variable.")


MONGO_URL = get_secret("MONGO_URL")
MONGO_DB_NAME = get_secret("MONGO_DB_NAME")
