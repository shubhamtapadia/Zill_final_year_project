from flask import Flask, flash, jsonify, redirect, render_template, request, session, g
from datetime import datetime
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")