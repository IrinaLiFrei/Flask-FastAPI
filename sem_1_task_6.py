# Задание №6
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

_users = [{'name': 'Ivan',
           'last_name': 'Ivanov',
           'age': '44',
           'average_mark': '4.8',
           },
          {'name': 'Petr',
           'last_name': 'Petrov',
           'age': '25',
           'average_mark': '5.0',
           }, ]

# context = {'users': _users}


@app.route('/table/')
def table():
    return render_template('sem_1_task_6_templ.html', users=_users)


if __name__ == '__main__':
    app.run(debug=True)
