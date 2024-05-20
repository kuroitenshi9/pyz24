from flask import Flask, redirect, url_for, render_template
from markupsafe import escape

app = Flask(__name__)
app.counter = 0

@app.route("/")
@app.route("/index")
def index():
    movies = [
        {'author' : 'Mel Gibson',
         'title' : 'Pasja'},
        {
        'author' : 'Bong',
        'title' : 'Parasite'}
    ]
    return render_template("index.html", title="Hello, hello", name="Rita", movies = movies)

@app.route('/articles')
def blog():
    articles = [
        {'author' : {'nickname' : 'John'},
         'title' : 'Beuatiful day in Poznan',
         'body' : 'Very random text about Poznan!'
        },
        {
        'author' : {'nickname': 'Susan'},
        'title' : 'Beuatiful day in Poznan',
         'body' : 'Very random text about Poznan!'
        }
    ]
    return render_template('articles.html', title="Awesome blog", articles=articles)

@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello/<name>')
def hello_user(name):
    return f'Hello {escape(name)}'

@app.route('/anonim')
def anonim():
    return redirect(url_for("hello", name='Guest'))

@app.route('/counter')
def visit_counter():
    app.counter += 1
    return f"Licznik odwiedzin: {app.counter}"

if __name__ == '__main__':
    app.run(debug=True)
