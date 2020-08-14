import requests
from wtforms.validators import ValidationError

BASE_URL = "http://api.postcodes.io/postcodes/"


class PostcodeClient:
    def validatePostcode(self, postcode):
        self.postcode = postcode
        data = requests.get(BASE_URL + postcode + "/validate").json()
        return data

    def lookupPostcode(self, postcode):
        self.postcode = postcode
        data = requests.get(BASE_URL + postcode).json()
        return data


class PostcodeValidator:
    def __init__(self, message=None):
        if not message:
            message = "Invalid postcode"
        self.message = message

    def __call__(self, form, field):
        Client = PostcodeClient()
        postcode = field.data
        check = Client.validatePostcode(postcode)
        if ~check:
            raise ValidationError(self.message)


def pcode():
    message = "Not a valid postcode"

    def _pcode(form, field):
        print(field.data)
        p = field.data
        Client = PostcodeClient()
        check = Client.validatePostcode(p)
        if check["result"] == False:
            raise ValidationError(message)

    return _pcode


def get_clean_postcode(valid_postcode):
    client = PostcodeClient()
    postcode_data = client.lookupPostcode(valid_postcode)
    return postcode_data["result"]["postcode"]
