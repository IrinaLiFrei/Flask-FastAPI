# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить" При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с результатом.

# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('1_1.html', **context)


@app.route('/', methods=['GET', 'POST'])
def arithmetic():
    if request.method == "POST":
        number_one = int(request.form.get('number_one'))
        number_two = int(request.form.get('number_two'))
        operation = request.form.get('operation')
        if operation == 'add':
            result = number_one + number_two
            return render_template('1_1_result.html', result=result)
        elif operation == 'sub':
            result = number_one - number_two
            return render_template('1_1_result.html', result=result)
        elif operation == 'mult':
            result = number_one * number_two
            return render_template('1_1_result.html', result=result)
        elif operation == 'div':
            if number_two == 0:
                result = 'Деление на ноль недопустимо'
                return render_template('1_1_result.html', result=result)
            else:
                result = number_one / number_two
                return render_template('1_1_result.html', result=result)


# TASK 2

@app.route('/', methods=['GET', 'POST'])
def age():
    if request.method == "POST":
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age < 18:
            return render_template('2_1.html', age=age, name=name)
        else:
            return render_template('2_2.html', age=age, name=name)
    return render_template('1_1_result.html')


if __name__ == '__main__':
    app.run(debug=True)