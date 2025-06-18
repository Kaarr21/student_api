from flask import Blueprint, request
from app.models import db, Course, CourseSchema

bp = Blueprint('courses', __name__, url_prefix='/courses')
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

@bp.route('/')
def list_courses():
    return courses_schema.dump(Course.query.all()), 200

@bp.route('/', methods=['POST'])
def create_course():
    data = request.json
    course = Course(title=data['title'])
    db.session.add(course)
    db.session.commit()
    return course_schema.dump(course), 201
