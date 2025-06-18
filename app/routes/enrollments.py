from flask import Blueprint, request
from app.models import db, Enrollment, EnrollmentSchema

bp = Blueprint('enrollments', __name__, url_prefix='/enrollments')
enrollment_schema = EnrollmentSchema()
enrollments_schema = EnrollmentSchema(many=True)

@bp.route('/', methods=['POST'])
def enroll_student():
    data = request.json
    enrollment = Enrollment(
        student_id=data['student_id'],
        course_id=data['course_id'],
        grade=data.get('grade')
    )
    db.session.add(enrollment)
    db.session.commit()
    return enrollment_schema.dump(enrollment), 201

@bp.route('/')
def list_enrollments():
    return enrollments_schema.dump(Enrollment.query.all()), 200

@bp.route('/<int:id>', methods=['DELETE'])
def unenroll(id):
    enrollment = Enrollment.query.get_or_404(id)
    db.session.delete(enrollment)
    db.session.commit()
    return {}, 204
