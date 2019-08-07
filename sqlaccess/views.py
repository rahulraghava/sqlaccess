"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from sqlaccess import app
import mysql.connector as qsl

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""



    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/db')
def contact():
    """Renders the contact page."""
    c = qsl.connect(host='172.16.0.2',user='rahul',password='rahul.281294',database='testDB')
    a = c.cursor()
    a.execute("SELECT * FROM Persons")
    b = a.fetchone()


    return ''.join(map(str,b))

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
