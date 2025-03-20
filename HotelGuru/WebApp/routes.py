from WebApp import app
from flask import render_template




user = {}

@app.route("/index")
@app.route("/")


def index():


    page = "Hotel Guru"   
    
   

    return render_template(
        'index.html',
        page_title = page,
    )
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
def root():
    return render_template("/index")