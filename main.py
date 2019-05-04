from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
#from flask_sqlalchemy import * 
from forms import RegistrationForm, LoginForm

#app = Flask(__name__)
app.config['SECRET_KEY'] = '86f41a39c3a243fd22d96228eaeb23a60df36e76'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(20))
#    email = db.Column(db.String(120))
#    image_file = db.Column(db.String(20))
#    password = db.Column(db.String(60))
#    posts = db.relationship('Post', backref='author', lazy=True)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#    def __repr__(self):
#        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
#
#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(100))
#    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
#    content = db.Column(db.Text)
#
#    def __repr__(self):
#        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
        {
            'author': 'Amos Corijn',
            'title': 'Programming - Week1',
            'content': """Learning to use Python via Flask. 
            \n - Used bootstrap starter template from getbootstrap.com 
            \n - Created home.html, about.html, and layout.html
            \n - Layout is used as template for all other pages.
            \n - Created different code snippets for specific things such as navigation.html, article.html, etc.
            \n - Learning basic HTML, Javascript, CSS to build webpage.
            \n - Actually don't have any idea what I am doing sometimes. Most times.
            \n - Ask Maks how to do some HTML things like remove line spacing.
            \n - Continuing to use VIM everyday - vimvtutor everyday
            \n - Completing regex questions everyday - hackerrank.com""",
            'date_posted': 'April 23, 2019'
            },
        {
            'author': 'Amos Corijn',
            'title': 'Programming - Week2',
            'content': """Second Week of Learning... Stuff...
            \n - Stuck with database on this site
            \n - Will try moving on to other parts of site
            \n - Will focus more this week on actual python code
            \n - Focus on Linux and Networking as well""",
            'date_posted': 'April 28, 2019'
            }
        ]
posts = posts[::-1]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) 

@app.route('/about')
def about():
    return render_template('about.html', title='About') 
@app.route('/memes')
def memes():
    return render_template('memes.html', title='Memes') 
@app.route('/gifs')
def gifs():
    return render_template('gifs.html', title='Gifs') 
@app.route('/network')
def network():
    return render_template('network.html', title='Network') 
@app.route('/youtube')
def youtube():
    return render_template('youtube.html', title='Youtube') 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account successfully created!', 'success')
        return redirect(url_for('/home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'amoscorijn@gmail.com' and form.password.data == 'password':
            flash('You are now logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
