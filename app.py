from flask import *
from flask import Flask # p1 dlaczego? czy * nie oznacza "wszystko"

app = Flask(__name__)

@app.route("/")
def me():
    return render_template("pierwsza.html")

@app.route("/contact")
def contact():
    return render_template("druga.html")

@app.route("/form")
def form():
    return render_template("formularz.html")