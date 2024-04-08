from flask import Flask, render_template, request, redirect, url_for
import supabase

app = Flask(__name__)

# Supabase configuration
url = 'https://rvcggegchnihvuowdqkw.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ2Y2dnZWdjaG5paHZ1b3dkcWt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI1NTMyNjksImV4cCI6MjAyODEyOTI2OX0.JCerxuRrRuHqNnYF1UN6osdsEY0xPxMxtqLVl9LV6eg'
supabase_client = supabase.create_client(url, key)

# Function to fetch student data from Supabase
def fetch_student_data():
    # Use Supabase client to fetch student data from the database
    response = supabase_client.from_('students').select('*').execute()
    if not supabase.check_error(response):  # Check for errors in the response
        student_data = response['data']
        return student_data
    else:
        # Handle error (e.g., print error message)
        print(f"Error fetching student data: {response['error']['message']}")  # Example error handling
        return []

# Function to fetch faculty data from Supabase
def fetch_faculty_data():
    # Use Supabase client to fetch faculty data from the database
    response = supabase_client.from_('faculty').select('*').execute()
    if not supabase.check_error(response):  # Check for errors in the response
        faculty_data = response['data']
        return faculty_data
    else:
        # Handle error (e.g., print error message)
        print(f"Error fetching faculty data: {response['error']['message']}")  # Example error handling
        return []

# Routes for student login
@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username and password match a student in the database
        # If match is found, redirect to student interface
        # Otherwise, render the login page again with an error message
        return redirect(url_for('student_interface'))
    return render_template('student_login.html')

# Routes for faculty login
@app.route('/faculty_login', methods=['GET', 'POST'])
def faculty_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username and password match a faculty member in the database
        # If match is found, redirect to faculty interface
        # Otherwise, render the login page again with an error message
        return redirect(url_for('faculty_interface'))
    return render_template('faculty_login.html')

# Routes for student interface
@app.route('/student_interface')
def student_interface():
    # Fetch student data from the database
    student_data = fetch_student_data()

    # Render the student interface template with the fetched data
    return render_template('student_interface.html', student_data=student_data)

# Routes for faculty interface
@app.route('/faculty_interface')
def faculty_interface():
    # Fetch faculty data from the database
    faculty_data = fetch_faculty_data()

    # Render the faculty interface template with the fetched data
    return render_template('faculty_interface.html', faculty_data=faculty_data)

if __name__ == '__main__':
    app.run(debug=True)
