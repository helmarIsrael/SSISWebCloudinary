from flask import Flask, redirect

from .main_menu.routes import main_menu
from .student.routes import student
from .course.routes import course
from .college.routes import college



app = Flask(__name__)

app.register_blueprint(main_menu)
app.register_blueprint(student)
app.register_blueprint(course)
app.register_blueprint(college)




@app.route('/')
def index():
    return redirect('/main_menu/')