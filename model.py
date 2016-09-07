"""Models and database functions for teacher_cms"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

####################################################################################################
# These teachers are the users

class Teacher (db.Model):
    """Teachers"""

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    


def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Teacher teacher_id=%s firstname=%s lastname=%s email=%s phonenumber=%s>"
                                                            % (self.teacher_id,
                                                                self.firstname,
                                                                self.lastname,
                                                                self.phonenumber))

#######################################################################################################



class Parent (db.Model):
    """Parents"""

    __tablename__ = "parents"

    parent_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=False)
    


def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Parent parent_id=%s firstname=%s lastname=%s email=%s phonenumber=%s>"
                                                            % (self.parent_id,
                                                            	self.firstname,
                                                                self.lastname,
                                                                self.phonenumber))


#######################################################################################################

class Student (db.Model):
    """Students"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    phonenumber = db.Column(db.String(15), nullable=True)
    


def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Student student_id=%s firstname=%s lastname=%s email=%s phonenumber=%s>"
                                                            % (self.student_id,
                                                                self.firstname,
                                                                self.lastname,
                                                                self.phonenumber))

#######################################################################################################

class Course (db.Model):
    """Courses"""

    __tablename__ = "courses"

    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    teacher_id = b.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    


def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Courses course_id=%s title=%s description=%s teacher_id=%s>"
                                                            % (self.course_id,
                                                                self.title,
                                                                self.description,
                                                                self.teacher_id))

#######################################################################################################

class Assignment (db.Model):
    """Assignments"""

    __tablename__ = "assignments"

    assign_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    date_due = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    


def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Assignments assign_id=%s title=%s description=%s date_due=%s teacher_id=%s>"
                                                            % (self.assign_id,
                                                                self.title,
                                                                self.description,
                                                                self.date_due,
                                                                self.teacher_id))

#######################################################################################################








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
