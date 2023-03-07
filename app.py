from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
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


@app.route('/add', methods=["GET", "POST"])
def add_new_pet():
    """add a new pet"""
    form = AddPetForm()
    species_options = [(pet.id, pet.species) for pet in Pet.query.all()]
    form.species.choices = species_options
    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=pet_name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)


@app.route('/pets/<int:pet_id>')
def show_pet_detail(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_detail.html", pet=pet)


@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def show_edit_page(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    species_options = [(pet.id, pet.species) for pet in Pet.query.all()]
    form.species.choices = species_options
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"Pet {pet.pet_name} updated!")
        return redirect(f"/pets/{pet_id}/edit")
    else:
        return render_template("edit_pet.html", form=form)
