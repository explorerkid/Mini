from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'student_request_system'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM tablename")
    data = cursor.fetchall()
    cursor.close()
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)