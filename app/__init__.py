from flask import Flask
from .models import db
from flask_migrate import Migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3001"])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    from .routes import students, courses, enrollments
    app.register_blueprint(students.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(enrollments.bp)

    return app
