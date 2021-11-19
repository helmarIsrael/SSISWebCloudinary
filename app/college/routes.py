from flask import Blueprint, render_template, redirect, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_database"
)

mycursor = db.cursor(buffered=True)

college = Blueprint('college', __name__, url_prefix='/main_menu/college_table')

@college.route('/college_add', methods=['post','get'])
def index():
    if request.method == 'POST' and 'college_code' in request.form:
        college_code = request.form['college_code']
        college = request.form['college']
        mycursor.execute("INSERT INTO `college` (`Code`, `Name`) "
                         "VALUES (%s,%s)",
                         (college_code, college))
        db.commit()
        return redirect("/main_menu/college_table")
    else:
        pass
    return render_template('college_add.html')