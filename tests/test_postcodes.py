import pytest
from property_price_model.postcodes import PostcodeClient


class TestClass:
    def test_validate_postcode_0(self):
        client = PostcodeClient()
        validator = client.validatePostcode("OX493 5NU")
        assert ~validator["result"]

    def test_validate_postcode_1(self):
        client = PostcodeClient()
        validator = client.validatePostcode("bl64ds")
        assert validator["result"]
