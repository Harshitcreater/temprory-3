from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #used to give access to templete and static files to flask

users = {
    "apeksha": {"password": "apeksha123", "page": "apeksha"},
    "ashwani": {"password": "ashwani123", "page": "ashwani"},
    "arjun":{"password":"arjun123","page":"arjun"}
}

@app.route('/') # define route of the url html file
def home():
    return render_template('login.html')#accessing the html file from template folder

@app.route('/login', methods=['POST'])
def login():
    
    username = request.form['username']# to enter username and password 
    password = request.form['password']

    
    if username in users and users[username]['password'] == password:# check whether the username is present in users or not if yes then it will check whether the password is correct or not 
    
        return redirect(url_for(users[username]["page"]))#if matched then it will take it to the wage page which is linked liked to it.
    else:
        
        return render_template('login.html', error="Invalid username or password!")#else remain on that page

@app.route('/apeksha')#define route to display html file
def apeksha():#define function and run further fuction detail
    return render_template('apeksha.html')# when particular function called it opens particular html file. 

@app.route('/ashwani')
def ashwani():
    return render_template('ashwani.html')
@app.route('/arjun')
def arjun():
    return render_template('arjun.html')
@app.route('/aschedule')
def aschedule():
    return render_template('aschedule.html')

def ashwanisirschedule():
    return render_template('ashwanisirschedule.html')
@app.route('/arjunsirschedule')
def arjunsirschedule():
    return render_template('arjunsirschedule.html')



if __name__ == '__main__':
    app.run(debug=True)
