from flask import render_template, url_for, flash, redirect
from flaskblog import app, db#, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

#posts = [
#        {
#            }
#        ]
#posts = posts[::-1]
#def create_app()
#    app = Flask(__name__)
#    Bootstrap(app)
#    return app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')#posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/hardware')
def hardware():
    return render_template('Hardware/hardware.html', title='Hardware')

@app.route('/hardware/RAM')
def RAM():
    return render_template('Hardware/RAM.html', title='RAM')

@app.route('/linux')
def linux():
    return render_template('Linux/linux.html', title='Linux')

@app.route('/linux/Arch')
def Arch():
    return render_template('Linux/Arch.html', title='Arch')

@app.route('/network')
def network():
    return render_template('Networking/network.html', title='Network')

@app.route('/random')
def random():
    return render_template('Random/random.html', title='Random')

@app.route('/random/ProjectPersonal')
def Projects():
    return render_template('Random/ProjectPersonal.html', title='Projects')

@app.route('/programming')
def youtube():
    return render_template('Programming/programming.html', title='Programming')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account successfully created! Please login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else rediruect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
