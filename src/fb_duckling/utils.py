from dotenv import load_dotenv
from os import path, getenv



env_path = "./.env"
env_default_path = "./.env.default"

if path.isfile(env_path):
    load_dotenv(env_path)
    print("loaded env variables from: {}".format(env_path))
elif path.isfile(env_default_path):
    load_dotenv(env_default_path)
    print("loaded env variables from: {}".format(env_default_path))
else:
    raise Exception("No .env file found please make sure that a .env file of the .env.default file"
                    "is present at the root of the project")


def get_default_port():
    return int(getenv("DEFAULT_PORT"))


def get_default_url():
    return str(getenv("DEFAULT_URL"))


def get_default_locale():
    return str(getenv("DEFAULT_LOCALE"))
