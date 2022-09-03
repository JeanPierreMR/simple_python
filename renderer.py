#coding=utf-8
from flask import Flask, render_template, request, redirect
import  json, requests
api_key = "bb753f5503816fa1b10cb0488e8016d7"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    debug=False
    app.run(host="0.0.0.0",debug=debug)



