from app import create_app
from app.models import db, Student, Course, Enrollment

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    s1 = Student(name="Alice")
    s2 = Student(name="Bob")

    c1 = Course(title="Math")
    c2 = Course(title="Science")

    db.session.add_all([s1, s2, c1, c2])
    db.session.commit()

    e1 = Enrollment(student_id=s1.id, course_id=c1.id, grade="A")
    e2 = Enrollment(student_id=s2.id, course_id=c2.id, grade="B")

    db.session.add_all([e1, e2])
    db.session.commit()
