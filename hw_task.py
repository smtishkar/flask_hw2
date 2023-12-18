# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан cookie-файл с данными пользователя, 
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя 
# и произведено перенаправление на страницу ввода имени и электронной почты.



from flask import Flask, flash, make_response, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = b'981e007ea2add77e2e0a24be6c77c395cc09e0d41e0d8e958304712d86b2075f'


@app.get('/')
def index():
    return render_template ('form_for_hw.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response(render_template("hello_page.html", name=name))
    session['username'] = request.form.get('username') or 'NoName'
    return response


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)