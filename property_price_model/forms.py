from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from property_price_model.postcodes import pcode

# pv = PostcodeValidator


class PropertyInputForm(FlaskForm):
    pcode = StringField("Postcode", validators=[pcode(), DataRequired()])
    sqft = IntegerField("Square Footage", validators=[DataRequired()])
    beds = IntegerField("Bedrooms", validators=[DataRequired()])
    submit = SubmitField("Submit data")
