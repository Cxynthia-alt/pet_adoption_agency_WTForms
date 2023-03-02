from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'
app.config['SECRET_KEY'] = "SECRET!"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    """show all pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route('/add')
def add_new_pet():
    """add a new pet"""
    form = AddPetForm()
    return render_template("add_pet_form.html", form=form)
