# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form.html')


@app.post('/')
def index_post():
    name = request.form.get('username')
    age = request.form.get('age')

    if int(age) >= 18:
        return render_template('success.html', context=name)
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)