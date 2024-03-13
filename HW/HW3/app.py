# Задание №7
# Создайте форму регистрации пользователей в приложении Flask. Форма должна содержать поля:
# имя, фамилия, email, пароль и подтверждение пароля. При отправке формы данные должны валидироваться
# на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.


from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from flask import render_template
from forms import RegForm


app = Flask(__name__)
app.config['SECRET_KEY'] = b'11c8c6695dd80a849122f1012ccb0562a055fe1ff6620fa097de02db4bd91d19'
csrf = CSRFProtect(app)


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
        password = form.password.data
        print(first_name, last_name, email, password)
        return "Вы успешно зарегистрировались!"
    return render_template('reg.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


