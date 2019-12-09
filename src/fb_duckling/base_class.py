from .utils import get_default_locale, get_default_url, get_default_port


class BaseClass(object):

    default_locale = get_default_locale()  # en_US
    default_url = get_default_url()  # http://0.0.0.0
    default_port = get_default_port()  # 8000
    default_timezone = get_default_timezone() # America/Los_Angeles

    def __init__(self, locale=default_locale, url=default_url, port=default_port, timezone=default_timezone):

        self.locale = locale or "en_US"
        self.url = url or "http://0.0.0.0"
        self.port = port or 8000
        self.timezone = timezone
