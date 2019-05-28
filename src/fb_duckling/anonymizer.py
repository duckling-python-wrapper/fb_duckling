from .base_class import BaseClass
from .duckling import Duckling
import re


class Anonymizer(BaseClass):

    default_anonymization_dict = {
        "email": "email",
        "phone-number": "phone"
    }

    def __init__(self, anonymization_dict=default_anonymization_dict,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.duckling = Duckling(*args, **kwargs)
        self.anonymization_dict = anonymization_dict

    def __call__(self, text, ignore_exp=[], fixed_len=True, locale=None, special_char="/"):
        result = self._duckling_request(text, locale or self.locale)
        anonymized_text = self._anonymize(
            result, text, ignore_exp=ignore_exp, fixed_len=fixed_len, special_char=special_char)
        return anonymized_text

    def _anonymize(self, result, text, ignore_exp=[], fixed_len=True, special_char="/"):
        """
        Text anonymization
        Warning: If fixed_len=False, it allows padding which use a special char,
                it might be incompatible with existing Tokenizer.

        :param result: result from duckling request
        :param text: text to anonymize
        :param ignore: list of value to ignore if found in result
        :param fixed_len: padding is disabled which means there is no indication 
                        on the length of the input data
        :param special_char: char to use in padding function

        :return: The anonymized version of the text
        """
        anonymized_text = text
        for res in result:
            if fixed_len:
                if res["dim"] in self.anonymization_dict.keys():
                    if not any(exp in res["body"] for exp in ignore_exp):
                        anonymized_text = re.sub(
                            res["body"], "personal_" + self.anonymization_dict[res["dim"]], anonymized_text)
            else:
                if res["dim"] in self.anonymization_dict.keys():
                    if not any(exp in res["body"] for exp in ignore_exp):
                        padding_len = len(res["body"])
                        anonymized_text = re.sub(
                            res["body"], self._add_padding(self.anonymization_dict[res["dim"]], padding_len, special_char), anonymized_text)

        return anonymized_text

    def _duckling_request(self, text, locale=None):
        result = self.duckling.request(text, locale=locale or self.locale)
        return result

    def _add_padding(self, key, length, special_char):
        return key.center(length, special_char)
