from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
































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
