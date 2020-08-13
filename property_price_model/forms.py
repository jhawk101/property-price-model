from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class PropertyInputForm(FlaskForm):
    pcode = StringField("Postcode")
    sqft = IntegerField("Square Footage")
    beds = IntegerField("Bedrooms")
    submit = SubmitField("Submit data")
