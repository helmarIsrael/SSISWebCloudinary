from flask import Blueprint, render_template, redirect, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_database"
)

mycursor = db.cursor(buffered=True)

course = Blueprint('course', __name__, url_prefix='/main_menu/course_table')

@course.route('/course_add', methods=['post','get'])
def index():
    mycursor.execute('SELECT `Name` FROM college')
    data = mycursor.fetchall()
    if request.method == 'POST' and 'course_code' in request.form:
        course_code = request.form['course_code']
        course = request.form['course']
        college = request.form['college']
        mycursor.execute("INSERT INTO `course` (`Course Code`, `Course Name`, `College`) "
                         "VALUES (%s,%s,%s)",
                         (course_code, course, college))
        db.commit()
        return redirect("/main_menu/course_table")
    else:
        pass
    return render_template('course_add.html', data=data)