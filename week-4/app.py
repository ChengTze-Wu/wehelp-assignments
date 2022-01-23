from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect, url_for

app = Flask(__name__)

app.secret_key = "jf8932fhuewifnd9o"

@app.route("/", methods=['GET'])
def index():
    return render_template("signin.html")

@app.route("/signin/", methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if username == "" or password == "":
            return redirect(url_for("error", message="請輸入帳號、密碼"))
        elif verify_account(username, password):
            return redirect(url_for("member"))
        else:
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

def verify_account(username, password):
    if username == "test" and password == "test":
        session["signin_state"] = 1
        return True


@app.route("/signout/", methods=['GET'])
def signout():
    session["signin_state"] = 0
    return redirect("/")

@app.route("/member/", methods=['GET'])
def member():
    if session["signin_state"] == 1:
        return render_template("member.html")
    return redirect("/")

@app.route("/error/", methods=['GET'])
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)

if __name__ == '__main__':
    app.run(port=3000)