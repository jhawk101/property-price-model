from property_price_model import db


class Sale(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    price = db.Column(db.Integer)
    date = db.Column(db.Date)
    postcode = db.Column(db.String(8))
    property_type = db.Column(db.String(1))
    new_build = db.Column(db.String(1))
    free_or_leasehold = db.Column(db.String(1))
    paon = db.Column(db.String(64))
    saon = db.Column(db.String(64))
    street = db.Column(db.String(64))
    locality = db.Column(db.String(64))
    town_city = db.Column(db.String(64))
    district = db.Column(db.String(64))
    county = db.Column(db.String(64))
    incode = db.Column(db.String(4))
    outcode = db.Column(db.String(4))

    def __repr__(self):
        return "<Sale {} {} {}> ".format(self.paon, self.saon, self.postcode)
