from fb_duckling import Anonymizer
import pytest


@pytest.fixture
def anonymizer():
    return Anonymizer()


class TestAnonymizer(object):

    def test_constructor(self, anonymizer):

        assert anonymizer.default_anonymization_dict == {
            "email": "email",
            "phone-number": "phone"
        }

    def test_anonymize(self, anonymizer):
        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"
        anonymized_text = "All work and no play makes personal_email a dull boy personal_phone"
        result = [{
            'body': 'jack@gmail.com',
            'start': 27,
            'value': {'value': 'jack@gmail.com'},
            'end': 41,
            'dim': 'email',
            'latent': False
        },
            {
            'body': '0102030405',
            'start': 53,
            'value': {'value': '0102030405'},
            'end': 63,
            'dim': 'phone-number',
            'latent': False
        }]
        assert anonymizer._anonymize(result, raw_text) == anonymized_text
        assert anonymizer(raw_text) == anonymized_text

    def test_anonymize_ignore(self, anonymizer):
        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"
        anonymized_text = "All work and no play makes personal_email a dull boy 0102030405"
        result = [{
            'body': 'jack@gmail.com',
            'start': 27,
            'value': {'value': 'jack@gmail.com'},
            'end': 41,
            'dim': 'email',
            'latent': False
        },
            {
            'body': '0102030405',
            'start': 53,
            'value': {'value': '0102030405'},
            'end': 63,
            'dim': 'phone-number',
            'latent': False
        }]
        assert anonymizer._anonymize(result, raw_text, ignore_exp=[
                                     "0102030405"]) == anonymized_text

    def test_anonymize_padding(self, anonymizer):
        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"
        anonymized_text = "All work and no play makes ////email///// a dull boy //phone///"
        result = [{
            'body': 'jack@gmail.com',
            'start': 27,
            'value': {'value': 'jack@gmail.com'},
            'end': 41,
            'dim': 'email',
            'latent': False
        },
            {
            'body': '0102030405',
            'start': 53,
            'value': {'value': '0102030405'},
            'end': 63,
            'dim': 'phone-number',
            'latent': False
        }]
        assert anonymizer._anonymize(
            result, raw_text, fixed_len=False) == anonymized_text
        assert anonymizer(raw_text, fixed_len=False) == anonymized_text

    def test_request(self, anonymizer):
        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"
        assert anonymizer._duckling_request(raw_text) is not None

