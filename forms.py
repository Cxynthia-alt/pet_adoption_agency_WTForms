from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    pet_name = StringField("Pet Name", validators=[
                           InputRequired(message="Please fill in pet name")])
    species = SelectField("Species")
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="age between 0-30")])
    notes = StringField("Notes")
    available = BooleanField("Available", validators=[InputRequired()])
