from flask import Flask, render_template, flash, request
import sqlite3
from config import login_required

app = Flask(__name__)

# Get sqlite3 database Conection
con = sqlite3.connect("gpa.db")
# create a cursor
cursor = con.cursor()

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    # If user requests login page
    if request.method == "GET":
        return render_template("login.html")
    
    # If user submits login credentials via form POST
    else:
        # Yet to implement
        pass
    
@app.route("/register", methods=["GET", "POST"])
def register():
    
    # if the user requests the register page
    if request.method == "GET":
        return render_template("register.html")
    
    # if the user submits registration form and submits through form POST
    else:
        # Yet to implement
        pass
    

@app.route("/ongoing")
@login_required
def ongoing():
    # Yet to implement
    pass


@app.route("/results")
@login_required
def results():
    # Yet to implement
    pass