from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/index')
def return_sample_page():
    return render_template('base.html', title='Название')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
