from flask import Flask, render_template, request, url_for, session, redirect
import os
from models import db, User
from forms import SignupForm, LoginForm, PatientForm

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'learningflask',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


db.init_app(app)

app.secret_key = "development-key"

#URL CSS thing
#CSS data would be stored in cache and would not update immediately.
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
#end URL CSS problem

@app.route("/", methods = ['POST', 'GET'])
def DataForm():
    form = PatientForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('DataForm.html', form=form)
        else:
            return "Successful"

    elif request.method == 'GET':
        return render_template('DataForm.html', form = form )


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            #Commented out until new database is made for this project.
            #newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            #db.session.add(newuser)
            #db.session.commit()

            #session['email'] = newuser.email
            #return redirect(url_for('home'))

            return "Successful"

    elif request.method == 'GET':
        return render_template('signup.html', form = form )

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    elif request.method == "GET":
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
