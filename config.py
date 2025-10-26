from flask import render_template, session, redirect
from functools import wraps
import sqlite3


def login_required(f):
    # decorate routes to require login
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def get_db():
    conn = sqlite3.connect("gpa.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn