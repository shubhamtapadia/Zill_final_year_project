from flask import Flask, flash, jsonify, redirect, render_template, request, session, g
from datetime import datetime
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///final_project_db_1.db"


#----Database------------

from sqlalchemy import DateTime, create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
from datetime import datetime
import os

#----DataBase Settings--------
engine = create_engine("sqlite:///final_project_db_1.db")
SessionLocal=scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = SessionLocal.query_property()
from model import (Customer)
db=SessionLocal()
Base.metadata.create_all(bind=engine)
#----DataBase Settings----^^^^----
app=Flask(__name__)
app.secret_key=os.urandom(5)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/shop")
def shop():
    return render_template("shop_1.html")

@app.route("/database")
def db_check():
    name="Shivaay"
    age=10
    data=Customer(name=name,age=age)
    db.add(data)
    db.commit()
    return f"Data saveed"

@app.route("/zeel")
def zeel2():
    return render_template("zeel.html")

@app.route("/shu")
def shubham():
    return render_template("shubham.html")

