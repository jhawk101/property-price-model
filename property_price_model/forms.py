from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from property_price_model.postcodes import pcode

# pv = PostcodeValidator


class PropertyInputForm(FlaskForm):
    pcode = StringField("Postcode", validators=[pcode(), InputRequired()])
    sqft = IntegerField("Square Footage", validators=[InputRequired()])
    beds = IntegerField("Bedrooms", validators=[InputRequired()])
    submit = SubmitField("Submit data")
