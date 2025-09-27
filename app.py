from flask import Flask, render_template, flash, request
import sqlite3

app = Flask(__name__)

# Get sqlite3 database Conection
con = sqlite3.connect("gpa.db")
# create a cursor
cursor = con.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", method=["GET", "POST"])
def login():
    
    # If user requests login page
    if request.method == "GET":
        return render_template("login.html")
    
    # If user submits login credentials via form POST
    else:
        # Yet to implement
        pass
    
@app.route("/register", method=["GET", "POST"])
def register():
    
    # if the user requests the register page
    if request.method == "GET":
        return render_template("register.html")
    
    # if the user submits registration form and submits through form POST
    else:
        # Yet to implement
        pass
    
@app.route("/ongoing")
def ongoing():
    # Yet to implement
    pass

@app.route("/results")
def results():
    # Yet to implement
    pass