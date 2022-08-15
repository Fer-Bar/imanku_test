from flask import render_template, session, request, flash, redirect, url_for
from polls.db_actions import check_user_exists, create_election
from werkzeug.security import check_password_hash
from polls import app

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'loggedin' not in session:
        email = request.form.get('email')
        password = request.form.get('password')
        user = check_user_exists(email)
        if user:
            pwd_hash = user[4]
            is_pass_correct = check_password_hash(pwd_hash, password)
            if is_pass_correct:
                session['loggedin'] = True
                session['id'] = user[0]
                session['email'] = user[3]
                flash(f"Account created successfully! You are now logged in as {user[1]}", category='success')
                return redirect(url_for('elections'))                   
            
            flash(f"Wrong credentials.", category='warning')
        else:              
            flash(f"User does not exist.", category='warning')                 
        return render_template('login.html')
    else:
        flash('You are logged in the page.', category='info')
        return redirect(url_for('elections'))

@app.route('/elections', methods=['GET', 'POST'])
def elections():
    if 'loggedin' in session:
        year = request.form.get('year')
        votecount = request.form.get('votecount')
        political_party = request.form.get('political_party')
        county = request.form.get('county')
        try:
            if request.method == 'POST':
                create_election(year, votecount, political_party, county)
                flash('Success creation.', category='success')
                return redirect(url_for('elections'))
        except Exception:           
            flash('Issues with the creation of the election', category='warning')
        return render_template('elections.html')
    else:
        flash("You need to log in for see election page.", category='warning')
        return redirect(url_for('login'))


