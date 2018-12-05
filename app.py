
from flask import Flask, render_template, request, redirect
# import test2

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("result.html")

if __name__=="__main__":
    # test2.init()
    app.run(debug=True)