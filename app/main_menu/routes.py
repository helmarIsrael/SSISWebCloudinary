from flask import Blueprint, render_template, redirect, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_database"
)

mycursor = db.cursor(buffered=True)

main_menu = Blueprint('main_menu', __name__, url_prefix='/main_menu')

@main_menu.route('/')
def index():
    return render_template('ssis_main.html')

@main_menu.route('/student_table', methods=['post','get'])
def students():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="student_database"
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM student_info')
    data = mycursor.fetchall()
    return render_template('student_table.html', data=data)

@main_menu.route('/course_table', methods=['post','get'])
def course():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="student_database"
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM course')
    data = mycursor.fetchall()
    return render_template('course_table.html', data=data)

@main_menu.route('/college_table', methods=['post','get'])
def college():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="student_database"
    )

    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM college')
    data = mycursor.fetchall()
    return render_template('college_table.html', data=data)