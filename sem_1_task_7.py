# Задание №7
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

_news = [{'title': 'Political news',
          'descr': 'Some political news',
          'date': '2024-02-02',
          },
         {'title': 'Social news',
          'descr': 'Some social news',
          'date': '2024-02-12',
          },
         {'title': 'Weather',
          'descr': 'Weather forecast',
          'date': '2024-02-12',
          }, ]


# context = {'users': _users}


@app.route('/news/')
def news():
    return render_template('sem_1_task_7_templ.html', news=_news)


if __name__ == '__main__':
    app.run(debug=True)
