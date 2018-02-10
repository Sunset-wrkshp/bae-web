from flask import Flask, render_template, request, url_for, session, redirect
import os
from models import db, User, Patient
from forms import SignupForm, LoginForm, PatientForm
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

POSTGRES = {
    'user': 'MECH_User',
    'pw': 'MECHMeeting',
    'db': 'B_Patients',
    'host': 'localhost',
    'port': '5432',
    #note: users must be given the correct privilages to edit database tables n such
}

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dyovhyczxffaic:36642e0405b1c01ee67c1e5af10435262535198dfd083f562d20ee3f5e9c40d3@ec2-54-225-255-132.compute-1.amazonaws.com:5432/d1kir75j338r7h'

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

#Patient entry data form
@app.route("/", methods = ['POST', 'GET'])
def DataForm():
    form = PatientForm()
    db.create_all()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('DataForm2.html', form=form)
        else:
            #Commented out until new database is made for this project.
            newpatient = Patient(form.first_name.data, form.last_name.data, form.age.data, form.s_pulse.data, form.e_pulse.data)
            db.session.add(newpatient)
            db.session.commit()
            #possible to do a "Patient submitted confirmation?" with name of last person
            #return render_template('DataForm.html', form=form)
            return redirect(url_for('DataForm'))
            #OK so this returns a blank page (good) while render_template returns the form with information still in it.
            #will it allow me to do the patient submitted confirmation?

    elif request.method == 'GET':
        return render_template('DataForm2.html', form = form )


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

#User login form (possibly a hidden page for admin access)
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

#logout page for admin
@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

#Output page
#So get first patient from the database.
@app.route("/display")
def display():
    search =  Patient.query
    latest = search.get(search.count())
    return render_template("display2.html", latest = latest, search = search)

if __name__ == "__main__":
    app.run(debug=True)
