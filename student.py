from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A dictionary to store users (for demo purposes)
users = {}

@app.route('/')
def login_page():
    return render_template('lgin.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users and users[username] == password:
        return redirect(url_for('student_page'))
    else:
        return render_template('lgin.html', error="Invalid username or password!")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if username in users:
            return render_template('register.html', error="Username already exists!")
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match!")
        
        users[username] = password
        return redirect(url_for('login_page'))
    
    return render_template('register.html')

@app.route('/student')
def student_page():
    return render_template('student.html')

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
    app.run(debug=True, port=5001)
