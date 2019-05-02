from fb_duckling import Anonymizer
import pytest

@pytest.fixture
def anonymizer():
    return Anonymizer()


class TestAnonymizer(object):

    def test_constructor(self, anonymizer):

        assert anonymizer.default_anonymization_dict == {
            "email": "personal_email",
            "phone-number": "personal_phone_number"
        }

    def test_call(self, anonymizer):

        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"
        anonimized_text = "All work and no play makes personal_email a dull boy personal_phone_number"

        assert anonymizer(raw_text) == anonimized_text