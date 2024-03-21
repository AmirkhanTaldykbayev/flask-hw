from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
from forms import RegistrationForm
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = b'aa5617f2ab95767b3ec1fe925bd446dec47fff78e229ab3ae937480cbcf15227'
csrf = CSRFProtect(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # to create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/mydatabase.db'  # work in project
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        if User.query.filter(User.email == form.email.data).all():
            flash('Пользователь с таким email уже существует!', 'danger')
            return redirect(url_for('register'))
        db.session.add(User(user_name=form.user_name.data, user_surname=form.user_surname.data, email=form.email.data,
                            hashed_psw=generate_password_hash(form.password.data)))
        db.session.commit()
        users = User.query.all()
        context = {'users': users, 'registered': True}
        return render_template('index.html', **context)
    return render_template('register.html', form=form)


@app.cli.command('create_db')
def one_time_run():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)