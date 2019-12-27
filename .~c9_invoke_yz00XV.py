from flask import Flask,render_template,flash,redirect,url_for
app = Flask(__name__)
from 
from forms import RegistrationForm,LoginForm
app.config['SECRET_KEY'] = '3tyyqty291757125ashfwqhvqjtvwq'
bycrpt = Bycrpt()
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