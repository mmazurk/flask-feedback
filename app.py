from flask import Flask, session, redirect, render_template, flash
from models import db, connect_db, User, Feedback
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LoginForm, FeedbackForm

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
    """redirect a user to the register page"""
    return redirect("/register")

@app.route("/register", methods = ['GET', 'POST'])
def register_user():
    """register a user in the database and save password"""

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)
        new_user.first_name = form.first_name.data
        new_user.last_name = form.last_name.data
        new_user.email = form.email.data
        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username  
        return redirect(f'/users/{username}')
    else:
        return render_template("register-user.html", form = form)

@app.route("/secret")
def show_secret_page():
    """show the secret page"""

    if session.get('username'):
        username = session.get('username')
        user = User.query.get_or_404(username)
        return render_template("secret-content.html", user = user)

    else:
        return redirect("/login")

@app.route("/login", methods = ['GET', 'POST'])
def login_user():
    """login the user"""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        authenticated_user = User.authenticate(username, password)
        if authenticated_user:
            flash("Good login, nice!", "primary")
            session["username"] = authenticated_user.username
            return redirect(f"/users/{username}")
        else: 
            form.username.errors.append('Invalid username/password')

    return render_template("login-user.html", form = form)

@app.route("/logout")
def logout_user():
    """logout the user"""

    session.pop('username', None)
    return redirect("/login")

@app.route("/users/<username>")
def show_user_information(username):
    """show information about a user"""

    if session.get('username') == username:
        user = User.query.get_or_404(username)
        feedback = user.feedback
        return render_template("user-page.html", user = user, feedback = feedback)

    else:
        return redirect("/login")
    
@app.route("/users/<username>/feedback/add", methods = ["GET", "POST"])
def add_feedback(username):

    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        feedback = Feedback(title = title, content = content, username = username)
        db.session.add(feedback)
        db.session.commit()
        return redirect(f"/users/{username}")

    status = "Add"
    user = User.query.get_or_404(username)
    return render_template("modify-feedback.html", user = user, form = form, status = status)


@app.route("/feedback/<int:feedback_id>/update")
def update_feedback(feedback_id):

    feedback = Feedback.query.get(feedback_id)
    username = feedback.user.username
    return render_template("secret-content.html", feedback = feedback, username = username)

# TODO: finish the route ("/feedback/<int:feedback_id>/update") so users can edit feedback
# TODO: figure out how to use the flash message in /login
# TODO: for all these, make sure only the logged in user can see and/or update
# TODO: do the delete below

# @app.route("/feedback/<int:feedback-id>/delete")
# def delete_feedback(username):

#     user = User.query.get_or_404(username)
#     return render_template("secret-content.html", user = user)

