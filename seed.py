"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app


# Create all tables
db.drop_all()  # drop all tables from database
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()  # delete everything
