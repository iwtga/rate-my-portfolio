from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

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
        name = request.form['username']
        password = request.form['password']
        if name not in database:
            return render_template('error.html', errorcode="User Not Found", errormessage="Username does not exist")
        else:
            if database[name] != password:
                return render_template('error.html', errorcode="Incorrect Password", erromessage="Password is Incorrect")
            else:
                return render_template('home.html')
        
    
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)