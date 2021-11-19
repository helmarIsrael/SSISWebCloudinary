from flask import Blueprint, render_template, redirect, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_database"
)

mycursor = db.cursor(buffered=True)

student = Blueprint('student', __name__, url_prefix='/main_menu/student_table')

@student.route('/student_add', methods=['post','get'])
def index():
    mycursor.execute('SELECT `Course Name` FROM course')
    data = mycursor.fetchall()
    if request.method == 'POST' and 'student_id' in request.form:
        student_id = request.form['student_id']
        name = request.form['name']
        year_level = request.form['year_level']
        gender = request.form['gender']
        course = request.form['course']
        mycursor.execute("INSERT INTO `student_info` (`Student ID`, `Name`, `Year Level`, `Gender`, `Course`) "
                         "VALUES (%s,%s,%s,%s,%s)",
                         (student_id, name, year_level, gender, code2))
        db.commit()
        return redirect("/main_menu/student_table")
    else:
        pass
    return render_template('student_add.html', data=data)