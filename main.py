# Задание №1
# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
#  Задание №2
# Дорабатываем задачу 1. Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".
# Задание №3
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
# Задание №4
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
# Задание №5
# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".


from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return 'Hello world!'


@app.route('/about/')
def about():
    return 'My name is Irina, I am 20 years old'


@app.route('/contact/')
def contact():
    return ('My phone: +7 7777777 '
            'My e-mail: 777@mail.ru')


@app.route('/sum/<int:number_1>/<int:number_2>/')
def get_sum(number_1, number_2):
    return str(number_1 + number_2)


@app.route('/length/<text>/')
def get_length(text):
    return str(len(text))


html = '''
<h1> Моя первая HTML-страница.</h1>
<p> Привет, мир! </p>
'''


@app.route('/main/')
def web():
    return html


if __name__ == '__main__':
    app.run(debug=True)
