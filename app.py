from flask import Flask, render_template, request, redirect
import sqlite3
import csv
import model

DBNAME = 'movie.db'
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("input.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    year = request.form["year"]
    month = request.form["month"]
    date = request.form["date"]
    type = request.form["type"]
    order = request.form["order"]
    return render_template("result.html", entries=model.get_input(year, month, date, type, order), 
    						year=year, month=month, date=date, type=type, order=order)

if __name__=="__main__":
    app.run(debug=True)

