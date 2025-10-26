from flask import Flask, render_template, flash, request, redirect, session
from flask_session import Session
import sqlite3
from config import login_required, get_db
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@login_required
def index():
    user_id = session.get('user_id')

    con = get_db()
    cursor = con.cursor()

    user_data = cursor.execute('SELECT * FROM student WHERE id = ?', (user_id,)).fetchone()
    greet = f"Welcome back, {user_data['firstname']} {user_data['lastname']}!👋" if user_data else ""
    cgpa = user_data['cgpa']

    con.close()

    return render_template("index.html", greeting=greet, cgpa=cgpa)


@app.route("/login", methods=["GET", "POST"])
def login():
    
    # If user requests login page
    if request.method == "GET":
        return render_template("login.html")
    
    # If user submits login credentials via form POST
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        
        con = get_db()
        cursor = con.cursor()

        result = cursor.execute('SELECT * FROM student WHERE email = ?', (email,)).fetchone()
        if not result or not check_password_hash(result["password_hashed"], password):
            flash("Invalid Username/Password Combination!")
            return redirect("/login")
        
        session['user_id'] = result["id"]
        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

    
@app.route("/register", methods=["GET", "POST"])
def register():
    
    # if the user requests the register page
    if request.method == "GET":
        return render_template("register.html")
    
    # if the user submits registration form and submits through form POST
    else:
        # take the user input, validate, register and redirect to home

        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("confirmation")

        # form validation
        if not (first_name and last_name and email and password and password_confirmation):
            flash("All fields are required!")
            return redirect("/register")
        if password != password_confirmation:
            flash("Passwords do not match!")
            return redirect("/register")

        password_hashed = generate_password_hash(password=password, method="pbkdf2", salt_length=16)

        con = get_db()
        cursor = con.cursor()

        exist_email = cursor.execute('SELECT * FROM student WHERE email = ?', (email,)).fetchone()


        if exist_email:
            flash("Email Already Exists!")
            con.close()
            return redirect("/register")
        
        # Insert new user
        cursor.execute('INSERT INTO student (email, password_hashed, firstname, lastname) VALUES (?, ?, ?, ?)', (email, password_hashed, first_name, last_name))
        con.commit()

        # Get user id
        user_data = cursor.execute('SELECT id FROM student WHERE email = ?', (email,)).fetchone()
        session["user_id"] = user_data["id"]

        con.close()
        return redirect("/")
    

@app.route("/ongoing")
@login_required
def ongoing():
    return render_template("ongoing.html")


@app.route("/results")
@login_required
def results():
    return render_template("results.html")

@app.route("/enroll")
def enroll():
    # Yet to implement
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)