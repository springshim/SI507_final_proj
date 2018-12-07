
from flask import Flask, render_template, request, redirect
import final_proj.py

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("result.html", entries=model.get_entries())

if __name__=="__main__":
    # test2.init()
    app.run(debug=True)