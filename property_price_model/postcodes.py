import requests
import pandas as pd
from wtforms.validators import ValidationError
import os


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


def get_epc_data(incode):
    """
    epc api called twice because it has a maximum return of 10000 done in 
    2x calls of 5000
    """

    key = os.getenv("EPC_KEY")
    headers = {"Authorization": "Basic " + key, "Accept": "application/json"}
    epc_url = (
        "https://epc.opendatacommunities.org/api/v1/domestic/search?postcode="
    )

    r = requests.get(epc_url + incode, headers=headers,)
    data = r.json()
    rows = data["rows"]

    r = requests.get(epc_url + incode + "&from=5000", headers=headers,)
    data = r.json()
    rows += data["rows"]

    epc = pd.DataFrame(data=rows, columns=data["column-names"])
    epc = epc.drop_duplicates(
        subset=["address1", "address2", "postcode"], keep="first"
    )

    return epc


def add_epc_key(epc_data, key_number=1):
    if key_number == 1:
        key = (
            epc_data["address1"]
            + " "
            + epc_data["address2"]
            + " "
            + epc_data["postcode"]
        ).str.lower()
    elif key_number == 2:
        key = (epc_data["address1"] + " " + epc_data["postcode"]).str.lower()
    else:
        raise ValueError

    key = key.str.replace(",", " ")
    key = key.str.replace("-", " ")
    key = key.str.replace(r"\s+", " ")

    return key


def add_combined_epc_key(epc_data, sales_key):
    epc = epc_data.copy()

    epc["key1"] = add_epc_key(epc, 1)
    epc["key2"] = add_epc_key(epc, 2)

    epc["key"] = None
    epc.loc[epc["key1"].isin(sales_key), "key"] = epc["key1"]
    epc.loc[(epc["key2"].isin(sales_key) & pd.isnull(epc["key"])), "key"] = epc[
        "key2"
    ]

    return epc["key"]


def add_land_reg_key(land_reg_data):
    key = (
        land_reg_data["saon"]
        + " "
        + land_reg_data["paon"]
        + " "
        + land_reg_data["street"]
        + " "
        + land_reg_data["postcode"]
    ).str.lower()

    key = key.str.replace(",", "")
    key = key.str.replace("-", " ")
    key = key.str.replace(r"\s+", " ")
    key = key.str.strip()

    return key


def augment_sales_data(sales, incode):
    sales[["postcode", "paon", "saon", "street"]] = sales[
        ["postcode", "paon", "saon", "street"]
    ].fillna("")

    epc = get_epc_data(incode)

    sales["key"] = add_land_reg_key(sales)
    epc["key"] = add_combined_epc_key(epc, sales["key"])

    merged = pd.merge(sales, epc, on="key", how="left")

    merged["total-floor-area"] = pd.to_numeric(merged["total-floor-area"])
    merged["number-heated-rooms"] = pd.to_numeric(merged["number-heated-rooms"])

    return merged
