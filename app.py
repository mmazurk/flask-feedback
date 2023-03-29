from flask import Flask, session, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from forms import RegisterForm

app = Flask(__name__)
app.app_context().push() 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

@app.route("/")
def redirect_user():
    return redirect("/register")

@app.route("/register", methods = ['GET', 'POST'])
def register_user():

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)
        new_user.first_name = form.first_name.data
        new_user.last_name = form.last_name.data
        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username  
        return redirect('/secret')
    else:
        return render_template("register-user.html", form = form)


# TODO -- test the POST part of the app.py route and see if it's working
# TODO -- then proceed with GET/login on 
