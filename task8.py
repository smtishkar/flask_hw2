# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".



from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = b'981e007ea2add77e2e0a24be6c77c395cc09e0d41e0d8e958304712d86b2075f'

@app.get('/')
def index():
    return render_template('form_for_task8.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    flash (f'Привет, {name}')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)