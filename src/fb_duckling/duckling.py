
"""
I took inspiration from the DucklingHttpExtractor from rasa_nlu
https://github.com/RasaHQ/rasa_nlu/blob/master/rasa_nlu/extractors/duckling_http_extractor.py
The idea was to create a standalone version from
this tool that could be used without rasa_nlu
"""

from .base_class import BaseClass
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import requests
import logging

logger = logging.getLogger(__name__)


class Duckling(BaseClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dim_list = [
            'amount-of-money', 'credit-card-number', 'distance', 'duration',
            'email', 'number', 'ordinal', 'phone-number', 'quantity',
            'temperature', 'time',  'time-grain', 'url', 'volume', 'regex'
        ]

        self.dim_onh = OneHotEncoder()
        self.dim_onh.fit(np.array(self.dim_list).reshape(-1, 1))

    def create_payload(self, text, locale):
        return {
            "text": text,
            "locale": locale
        }

    def request(self, text, locale=None):

        headers = {"Content-Type": "application/x-www-form-urlencoded; "
                                   "charset=UTF-8"}

        # Payload
        payload = self.create_payload(text=text, locale=locale or self.locale)

        # Perform Request
        response = requests.post(
            "{0}:{1}/parse".format(self.url, self.port),
            data=payload,
            headers=headers
        )

        try:
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(
                    "Failed to get a proper response from Duckling\n"
                    "status_code: {0},\nResponse: {1}".format(
                        response.status_code, response.text
                    ))
                return []
        except requests.exceptions.ConnectionError as e:
            logger.error("Could not connect to duckling, please make sure that"
                         "the Duckling http server is on:\n"
                         "https://github.com/facebook/duckling\n"
                         "Error: {0}".format(e))

    def extract_dims(self, text, locale=None):
        return {
            x["dim"] for x in self.request(text=text, locale=locale or self.locale)
        }

    def contains_dim(self, text, locale=None):
        return self.dim_onh.transform(
            [list(self.extract_dims(text=text, locale=locale or self.locale))]
        )
