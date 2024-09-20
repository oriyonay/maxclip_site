import config
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/competition')
def competition():
    return render_template('competition.html')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


@app.route('/participate')
def participate():
    return render_template('participate.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
