from polls import app
from flask import render_template, session, request, flash, redirect, url_for
from polls.connection import get_connection
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        con = get_connection()
        email = request.form.get('email')
        password = request.form.get('password')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM coordinator WHERE email = '{email}'") #Check the user exists.
        user = cur.fetchone()
        cur.close()
        con.close()
        if user:
            pwd_hash = user[4]
            is_pass_correct = check_password_hash(pwd_hash, password)
            if is_pass_correct:
                session['loggedin'] = True
                session['id'] = user[0]
                session['email'] = user[3]
                flash(f"Account created successfully! You are now logged in as {user[1]}", category='success')
                return redirect(url_for('elections'))                   
            else:
                flash(f"Wrong credentials.", category='error')
                return redirect(url_for('login')) 
        else:           
            flash(f"User does not exist.", category='error')
            return redirect(url_for('login'))
                   
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/elections', methods=['GET', 'POST'])
def elections():
    if request.method == 'POST':
        con = get_connection()
        year = request.form.get('year')
        votecount = request.form.get('votecount')
        political_party = request.form.get('political_party')
        code_county = request.form.get('code_county')
        # Check if user is loggedin
        if 'loggedin' in session:
            with con.cursor() as cur:
                year, votecount, political_party, code_county = year, votecount, political_party, code_county
                cur.execute("INSERT INTO election(year, votecount, political_party, code_county) VALUES (%s, %s, %s, %s)",
                        (year, votecount, political_party, code_county))
                con.commit()
                con.close()
                flash('Success creation.')
                return redirect(url_for('elections'))
        flash('Issues with the creation.')
        return redirect(url_for('elections'))
    if request.method == 'GET':
        return render_template('elections.html')

