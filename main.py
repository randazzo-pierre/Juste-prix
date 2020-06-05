#!/usr/bin/env python
# -*- coding: utf­-8 ­-*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/hello/<n>")
def hello_name(n):
    return render_template("hello.html", name=n)


if __name__ == "__main__":
    app.run()
