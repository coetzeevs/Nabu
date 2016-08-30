from app import app
from app import dbconnect
from app import subfunctions
from app import tabledef
from app import dbconnect
from app import subfunctions
from app import tabledef
from flask import flash, redirect, render_template, request, session, abort, url_for
import pandas as pd
import os
from .dbconnect import connect_login, register_user, add_customer2, get_all_customers, update_customer2, update_customer3,get_customers

@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if request.form['btn'] == 'Bar_SCV':
                barname = request.form['barishname']
                return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
    return render_template('index.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form['btn'] == 'Bar_SCV':
            barname = request.form['barishname']
            return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
    return render_template('navbar.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        temp_name = request.form['username']
        temp_password = request.form['password']
        register_user(temp_name, temp_password)
        return redirect(url_for('home'))
    return render_template('register.html', error=error)


@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    error = None
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            print('1')
            # if request.form['btn'] == 'Bar_SCV':
            #     barname = request.form['barishname']
            #     return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
            # else:
            province = request.form['province']
            area = request.form['area']
            bar = request.form['bar']
            person = request.form['person']
            number = request.form['number']
            email = request.form['email']
            print(email)
            add_customer2(province, area, bar, person, number, email)
            return render_template('customer_added.html', error=error)
        return render_template('add_customer.html', error=error)


@app.route('/display', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        if request.form['btn'] == 'Bar_SCV':
            barname = request.form['barishname']
            return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
    location = 'platinum_offers.xlsx'

    # Parse the excel file
    df = get_all_customers()
    df.index.name = None
    # females = df.loc[df.Gender == 'f']
    # males = df.loc[df.Gender == 'm']
    return render_template('display_table.html', tables=[df.to_html(classes='male')],
                           titles=['na', 'New Customers', 'Existing Customers'])


@app.route('/login_2', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            x = request.form['username']
            y = request.form['password']
            z = connect_login(x, y)
            if z == 0:
                error = 'Wrong UserName or Password'
            else:
                session['logged_in'] = True
                return redirect(url_for('home'))
        else:
            return redirect(url_for('register'))
    return render_template('login2.html', error=error)


@app.route('/update_customer', methods=['GET', 'POST'])
def update_last_seen():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if request.form['btn'] == 'Bar_SCV':
                barname = request.form['barishname']
                return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
            if request.form['btn'] == 'Update Last Called':
                barname = request.form['barname']
                dated = request.form['dated']
                update_customer2(barname, dated)
                return render_template('customer_added.html')
            else:
                barname2 = request.form['barname2']
                update_customer3(barname2)
                return render_template('customer_added.html')
    return render_template('update.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/profile/<name>")
def profile(name):
    x = name
    y = get_customers(x)
    p = y.iat[0, 0]
    return render_template("profile.html", y=y)


@app.route('/test')
def test():
    POST_USERNAME = "python"
    POST_PASSWORD = "python"

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object not found " + POST_USERNAME + " " + POST_PASSWORD
