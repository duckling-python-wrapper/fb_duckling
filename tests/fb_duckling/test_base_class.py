from fb_duckling import BaseClass
import pytest


class TestBaseClass():

    def test_constructor(self):

        # Base test
        base_class = BaseClass()
        assert base_class.locale == "en_US"
        assert base_class.url == "http://0.0.0.0"
        assert base_class.port == 8000

        # Modification test
        base_class_mod = BaseClass(locale="fr_FR", url="http://127.0.0.0", port=8001)
        assert base_class_mod.locale == "fr_FR"
        assert base_class_mod.url == "http://127.0.0.0"
        assert base_class_mod.port == 8001