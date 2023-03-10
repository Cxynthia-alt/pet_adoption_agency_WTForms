from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        return f"<Pet id={self.id} name={self.name}>"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(25), nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String(50))
    available = db.Column(db.Boolean, nullable=False, default=True)
