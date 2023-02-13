from flask import render_template, request, redirect
from flask import Flask

app = Flask(__name__)

@app.route("/mypage/me")
def me():
    return render_template("pierwsza.html")


@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       return render_template("druga.html")
    elif request.method == 'POST':
       print(request.form)
       return redirect("/mypage/me")
