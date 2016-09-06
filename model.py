"""Models and database functions for teacher_cms"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

##############################################################################################
# These teachers are the users

class Teacher (db.Model):
    """Teachers"""

    __tablename__ = "teachers"

	teacher_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    classes = db.Column(db.Integer, db.ForeignKey('classes.class_id'), nullable=False)
    passenger_location = db.Column(db.String(100), nullable=False)
    passenger_destination = db.Column(db.String(100), nullable=False)
    pick_up_time = db.Column(db.DateTime, nullable=False)
    passenger_rating = db.Column(db.Integer, nullable=True)
    driver_rating = db.Column(db.Integer, nullable=True)


	#define relationship to the driver
    driver = db.relationship("Driver", backref="rides")

    #define relationship to the user
    passenger = db.relationship("Passenger", backref="rides")
























################################################################################
def connect_to_db(app, databaseURI='postgresql:///teachercms'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = databaseURI
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
