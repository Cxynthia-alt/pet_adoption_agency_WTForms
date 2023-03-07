"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app


# Create all tables
db.drop_all()  # drop all tables from database
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()  # delete everything

pet1 = Pet(name="scrubby", species="dog",
           photo_url="https://unsplash.com/photos/igY9Ox92R5M", age=2, available=True)
pet2 = Pet(name="milk", species="cat", photo_url="https://images.unsplash.com/photo-1615789591457-74a63395c990?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8a2l0dHl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
           age=1, notes="need special care", available=True)


db.session.add(pet1)
db.session.add(pet2)
db.session.commit()
