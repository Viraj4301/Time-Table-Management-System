# Import all important libraries
from flask import *
from flask_sqlalchemy import SQLAlchemy
import re

# initialize first flask
app = Flask(__name__)
app.secret_key = 'xyzsdfg'

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user-system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Users = SQLAlchemy(app)


class timeTB(Users.Model):
    id = Users.Column(Users.Integer, primary_key=True, autoincrement = True)
    stime = Users.Column(Users.Integer)
    time = Users.Column(Users.Integer)
    venue = Users.Column(Users.String(50))
    course = Users.Column(Users.String(50))
    c_color = Users.Column(Users.String(50))
    whichday = Users.Column(Users.String(50))
    faculty = Users.Column(Users.String(50))

# Define User model
class User(Users.Model):
    id = Users.Column(Users.Integer, primary_key=True)
    name = Users.Column(Users.String(50), nullable=False)
    email = Users.Column(Users.String(50), unique=True, nullable=False)
    password = Users.Column(Users.String(50), nullable=False)

'''def __init__(self, name, email, password):
   self.name = name
   self.email = email
   self.password = password
'''

# Make login function for login and also make
# session for login and registration system
# and also fetch the data from database
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    admin_email = 'admin@sot.pdpu.ac.in'
    admin_pswd = 'qwerty'
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        if email == admin_email and password == admin_pswd:
            return render_template('admin.html', message=message)
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['loggedin'] = True
            session['userid'] = user.id
            session['name'] = user.name
            session['email'] = user.email
            message = 'Logged in successfully!'
            return render_template('user.html', message=message)
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message=message)

# Make function for logout session
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/uindex', methods=['GET', 'POST'])
def uindex(): 
    return render_template('uindex.html')

@app.route('/index1', methods=['GET','POST'])
def index1():  
    return render_template('index1.html')

@app.route('/index1call', methods=['GET','POST'])
def index1call():
    if request.method == 'POST':
        print("Success")
        data = request.json
        stime = data.get('stime')
        time = data.get('time')
        venue = data.get('venue')
        course = data.get('course')
        ccolor = data.get('c_color')
        whichday = data.get('whichday')
        faculty  = data.get('faculty')
        print(stime)
        new_time = timeTB(stime=stime, time= time, venue=venue, course = course, c_color = ccolor, whichday = whichday, faculty = faculty )
        Users.session.add(new_time)
        Users.session.commit()
    return 'Data saved successfully!'

# Make a register session for registration session
# and also connect to database to code for access login
# and for completing our login session and making some
# flashing massage for error
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        account = User.query.filter_by(email=email).first()
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not userName or not password or not email:
            message = 'Please fill out the form!'
        else:
            new_user = User(name=userName, email=email, password=password)
            Users.session.add(new_user)
            Users.session.commit()
            message = 'You have successfully registered!'
    elif request.method == 'POST':
        message = 'Please fill out the form!'
    return render_template('register.html', message=message)




# run code in debug mode, uncomment below is running for the first time to create the table.

'''with app.app_context():
    Users.create_all()
'''

if __name__ == "__main__":
    #Users.create_all()
    app.run(debug=True)
