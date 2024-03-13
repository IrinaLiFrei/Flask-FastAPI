# Задание №8
# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован

from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from flask import render_template
from forms import RegForm
from models import db, User
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = b'11c8c6695dd80a849122f1012ccb0562a055fe1ff6620fa097de02db4bd91d19'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_db.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == "POST" and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template('success.html', first_name=first_name)
    return render_template('reg.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


