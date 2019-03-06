
"""
I took inspiration from the DucklingHttpExtractor from rasa_nlu
https://github.com/RasaHQ/rasa_nlu/blob/master/rasa_nlu/extractors/duckling_http_extractor.py
The idea was to create a standalone version from this tool that could be used without rasa_nlu
"""

from .utils import get_default_locale, get_default_url, get_default_port
import requests
import logging

logger = logging.getLogger(__name__)


class Duckling(object):

    default_locale = get_default_locale() #"en_US"
    default_url = get_default_url() #"http://0.0.0.0"
    default_port = get_default_port() #8000

    def __init__(self, locale=default_locale, url=default_url, port=default_port):

        self.locale = locale
        self.url = url
        self.port = port

        self.dim_list = ['amount-of-money', 'distance', 'time', 'ordinal']

    def create_payload(self, text, locale):
        return {
            "text": text,
            "locale": locale
        }

    def request(self, text, locale=default_locale, url=default_url, port=default_port):

        headers = {"Content-Type": "application/x-www-form-urlencoded; "
                                   "charset=UTF-8"}

        # Payload
        payload = self.create_payload(text=text, locale=locale)

        # Perform Request
        response = requests.post("{0}:{1}/parse".format(url, port), data=payload, headers=headers)

        try:
            if response.status_code == 200:
                return response.json()
            else:
                logger.error("Failed to get a proper response from Duckling\nstatus_code: {0},\nResponse: {1}".format(
                    response.status_code, response.text
                ))
                return []
        except requests.exceptions.ConnectionError as e:
            logger.error("Could not correct to duckling, please make sure that the Duckling http server is on:\n"
                         "https://github.com/facebook/duckling\n"
                         "Error: {0}".format(e))




    def contains_dim(self):
        #TODO
        pass



