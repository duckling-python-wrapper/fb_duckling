from fb_duckling import Duckling
import pytest
import numpy as np


@pytest.fixture
def duckling():
    return Duckling()


class TestDuckling(object):

    def test_constructor(self, duckling):

        assert duckling.dim_list == [
            'amount-of-money', 'credit-card-number', 'distance', 'duration',
            'email', 'number', 'ordinal', 'phone-number', 'quantity',
            'temperature', 'time',  'time-grain', 'url', 'volume', 'regex'
        ]

    def test_create_payload(self, duckling):
        locale = "fr_FR"
        raw_text = "All work and no play makes jack@gmail.com a dull boy 0102030405"

        assert duckling.create_payload(raw_text, locale) == {
            "text": raw_text,
            "locale": locale
        }

    def test_request(self, duckling):
        raw_text = "hello jack@gmail.com"
        assert duckling.request(raw_text) == [
            {
                'body': 'jack@gmail.com',
                'start': 6,
                'value': {'value': 'jack@gmail.com'},
                'end': 20,
                'dim': 'email',
                'latent': False
            }
        ]

    def test_extract_dims(self, duckling):
        raw_text = "hello jack@gmail.com"
        assert duckling.extract_dims(raw_text) == {'email'}

    def test_contains_dim(self, duckling):
        raw_text = "hello jack@gmail.com"

        assert np.array_equal(
            duckling.contains_dim(raw_text).toarray(),
            np.array([[0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
        )
