from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Users and their data for the teacher section
users1 = {
    "apeksha": {"password": "apeksha123", "page": "apeksha"},
    "ashwani": {"password": "ashwani123", "page": "ashwani"},
    "arjun": {"password": "arjun123", "page": "arjun"}
}

# Users dictionary for the student section
users2 = {}

@app.route('/')  # Home page that will guide user to the login page based on their role
def home():
    # This could be a simple welcome page with links to login as student or teacher.
    return render_template('index.html')  # Custom home page with links to login as student or teacher
  # Separate login page for students

@app.route('/login1')  # Login page for teachers
def teacher_login():
    return render_template('login.html')  # Separate login page for teachers

@app.route('/login1', methods=['POST'])  # Login route for the teacher section
def login1():
    username = request.form['username']
    password = request.form['password']

    if username in users1 and users1[username]['password'] == password:
        return redirect(url_for(users1[username]["page"]))  # Redirect to teacher page
    else:
        return render_template('login.html', error="Invalid username or password!")

@app.route('/login2')  # Login page for students
def student_login():
    return render_template('lgin.html')

@app.route('/login2', methods=['POST'])  # Login route for the student section
def login2():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users2 and users2[username] == password:  # Correct comparison
        return redirect(url_for('student_page'))  # Redirect to student page
    else:
        return render_template('lgin.html', error="Invalid username or password!")


@app.route('/register', methods=['GET', 'POST'])  # Registration page for the student section
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if username in users2:
            return render_template('register.html', error="Username already exists!")
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match!")

        users2[username] = password
        return redirect(url_for('student_login'))  # Redirect to the login page for students after registration
    
    return render_template('register.html')

@app.route('/student')  # Student page after successful login
def student_page():
    return render_template('student.html')

# Routes for teacher section
@app.route('/apeksha')
def apeksha():
    return render_template('apeksha.html')

@app.route('/ashwani')
def ashwani():
    return render_template('ashwani.html')

@app.route('/arjun')
def arjun():
    return render_template('arjun.html')

@app.route('/aschedule')
def aschedule():
    return render_template('aschedule.html')

@app.route('/ashwanisirschedule')
def ashwanisirschedule():
    return render_template('ashwanisirschedule.html')

@app.route('/arjunsirschedule')
def arjunsirschedule():
    return render_template('arjunsirschedule.html')

# Routes for student section
@app.route('/apekshakaul')
def apekshakaul():
    return render_template('apekshakaul.html')

@app.route('/ashwin')
def ashwin():
    return render_template('ashwin.html')

@app.route('/arjunkumar')
def arjunkumar():
    return render_template('arjunkumar.html')

@app.route('/apstudent')
def apstudent():
    return render_template('apstudent.html')

@app.route('/ashstudent')
def ashstudent():
    return render_template('ashstudent.html')

@app.route('/arjstudent')
def arjstudent():
    return render_template('arjstudent.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
