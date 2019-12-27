from flask import Flask,render_template,flash,redirect,url_for
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
app.config['SECRET_KEY'] = '3tyyqty291757125ashfwqhvqjtvwq'
app.config['SQLALCHEMY_DATABASE_URL'] ='sqlite://site.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    userna= db.Column(db.String(120),unique = True,nullable = False)
    image_file = db.Column(db.String(20),nullable = False,default = 'default.jpg')
    password = db.Column(db.String(60),nullable=False)
    d
post= [
    {'name':'Jack',
    'place':'New Jersey',
    'allergies':'Peanuts'},
    {'name':'Jill',
    'place':'New York',
    'allergies' : 'None'
    }
]
@app.route("/")
def home():
    return render_template('home.html',people = post)
@app.route('/register/',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    print(type(form))
    if form.validate_on_submit():
        flash("Account created for " + form.username.data,'Completed!')
        return redirect(url_for('login'))
    return render_template('register.html',form = form)
@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/donate/')
def donate():
    return render_template('donate.html')
@app.route('/nice/')

def nice():
    import flask_wtf
    
    return "nice SUCCESS!"