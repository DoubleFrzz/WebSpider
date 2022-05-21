import pymysql
from flask import Flask, render_template, request
from sqlHelper import SqlHelper

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/movie')
def movie():
    sqlHelper = SqlHelper()
    data = sqlHelper.select_all()
    return render_template("movie.html", data=data)


@app.route('/comment')
def comment():
    return render_template("comment.html")


if __name__ == '__main__':
    app.run(debug=True)
