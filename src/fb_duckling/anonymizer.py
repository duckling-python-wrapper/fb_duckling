from .base_class import BaseClass
from .duckling import Duckling
import re


class Anonymizer(BaseClass):

    default_anonymization_dict = {
        "email": "personal_email",
        "phone-number": "personal_phone_number"
    }

    def __init__(self, anonymization_dims=("email", "phone-number"),
                 anonymization_dict=default_anonymization_dict,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.duckling = Duckling(*args, **kwargs)
        self.anonymization_dims = anonymization_dims
        self.anonymization_dict = anonymization_dict

    def __call__(self, text, locale=None):

        result = self.duckling.request(text, locale=locale or self.locale)

        anonymized_text = text.copy()
        for res in result:
            if res["dim"] in self.anonymization_dims:
                anonymized_text = re.sub(res["body"], self.anonymization_dict[res["dim"]], anonymized_text)

        return anonymized_text
