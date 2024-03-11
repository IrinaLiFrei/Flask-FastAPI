# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('1.html', **context)


@app.route('/contact/')
def contact():
    context = {'title': 'Контакты'}
    return render_template('1-1.html', **context)


@app.route('/catalog/')
def catalog():
    context = {'title': 'Каталог товаров'}
    return render_template('1-2.html', **context)

@app.route('/women/')
def women():
    context = {'title': 'Женская одежда'}
    return render_template('1-3.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
