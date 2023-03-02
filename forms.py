from flask_wtf import Flaskform
from wtforms import StringField, FloatField

class AddPetForm(Flaskform):
    pet_name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = FloatField("Age")
    notes = StringField("Notes")
