# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_for_task7.html')


@app.post('/')
def index_post():
    number = request.form.get('number')
    result = int(number) * int (number)
    return render_template('success_for_task7.html', number=number, context=result)


if __name__ == '__main__':
    app.run(debug=True)