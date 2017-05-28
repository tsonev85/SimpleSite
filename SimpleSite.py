from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/test')
def hello_world():
    return render_template('index.html')


@app.route('/home', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
