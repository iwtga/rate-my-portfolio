from flask import Flask, render_template, url_for, redirect, request
import pyrebase

app = Flask(__name__)

config ={
    "apiKey": "AIzaSyDHpOYyNgtYcrnCORHLHLyPDK4bdgY4_Vs",
    "authDomain": "ratemyportfolio-39e05.firebaseapp.com",
    "databaseURL": "https://ratemyportfolio-39e05-default-rtdb.firebaseio.com/",
    "projectId": "ratemyportfolio-39e05",
    "storageBucket": "ratemyportfolio-39e05.appspot.com",
    "messagingSenderId": "115042671407",
    "appId": "1:115042671407:web:403f102924080cf89b1fda",
    "measurementId": "G-RMQFGMEQYV"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

database = {'warren': 'warren271001'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.errorhandler(404) 
def not_found(e): 
  return render_template("error.html", errorcode='404', errormessage="Page Not Found")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/form_login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if auth.sign_in_with_email_and_password(email,password):
            return render_template('home.html')
        else:
            return  render_template('error.html')
        
@app.route('/signup')
def signuppage():
    return render_template('signup.html')

@app.route('/form_signup', methods=["POST","GET"])
def signup():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        auth.create_user_with_email_and_password(email,password)
        return render_template('home.html')
        
    

if __name__ == "__main__":
    app.run(debug=True)