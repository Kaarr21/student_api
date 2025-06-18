from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

# Association Table
class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String)
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    enrollments = db.relationship('Enrollment', back_populates='student', cascade="all, delete")

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    enrollments = db.relationship('Enrollment', back_populates='course', cascade="all, delete")

class EnrollmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Enrollment
        include_fk = True

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        include_relationships = True
        load_instance = True

class CourseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_relationships = True
        load_instance = True

