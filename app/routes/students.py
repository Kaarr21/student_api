from flask import Blueprint, request, jsonify
from app.models import db, Student, StudentSchema

bp = Blueprint('students', __name__, url_prefix='/students')
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@bp.route('/')
def list_students():
    return students_schema.dump(Student.query.all()), 200

@bp.route('/<int:id>')
def get_student(id):
    student = Student.query.get_or_404(id)
    return student_schema.dump(student), 200

@bp.route('/', methods=['POST'])
def create_student():
    data = request.json
    student = Student(name=data['name'])
    db.session.add(student)
    db.session.commit()
    return student_schema.dump(student), 201
