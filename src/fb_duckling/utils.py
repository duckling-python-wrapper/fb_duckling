from dotenv import load_dotenv
from os import getenv
load_dotenv()


def get_default_port():
    return int(getenv("DEFAULT_PORT"))


def get_default_url():
    return str(getenv("DEFAULT_URL"))

def get_default_locale():
    return str(getenv("DEFAULT_LOCALE"))
