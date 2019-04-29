import simplejson as json
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '86f41a39c3a243fd22d96228eaeb23a60df36e76'

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
            'content': 'Second post content',
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
