from flask import render_template, request, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user
from app.models import User


@app.route('/')
def home():
    return redirect('admin')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        candidate = User.query.filter_by(email=form.email.data).first()
        if candidate and candidate.password == form.password.data:
            login_user(candidate)
            return redirect('admin')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(form.data)
        del data['confirm']
        del data['register']
        email = User.query.filter_by(email=data['email']).first()
        if email:
            return render_template('register.html', form=form, error='Email is already exist')
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
