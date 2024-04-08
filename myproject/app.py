from flask import Flask, render_template
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_login')
def student_login():
    return render_template('student_login.html')

@app.route('/faculty_login')
def faculty_login():
    return render_template('faculty_login.html')

@app.route('/student_interface')
def student_interface():
    # Fetch student ID from database
    cur = mysql.connection.cursor()
    cur.execute("SELECT student_id FROM students WHERE student_name = %s", ('Student Name',))
    student_id = cur.fetchone()
    cur.close()

    return render_template('student_interface.html', student_id=student_id)

@app.route('/faculty_interface')
def faculty_interface():
    # Fetch faculty ID from database
    cur = mysql.connection.cursor()
    cur.execute("SELECT faculty_id FROM faculty WHERE faculty_name = %s", ('Faculty Name',))
    faculty_id = cur.fetchone()
    cur.close()

    return render_template('faculty_interface.html', faculty_id=faculty_id)

if __name__ == '__main__':
    app.run(debug=True)
