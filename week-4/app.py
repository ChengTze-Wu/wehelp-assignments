from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect, url_for

app = Flask(__name__)

app.secret_key = "jf8932fhuewifnd9o"

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        endpoint, message = verify_account(username, password)
        return redirect(url_for(endpoint=endpoint, message=message))
    return render_template("signin.html")


@app.route("/", methods=['GET'])
@app.route("/signin/", methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        endpoint, message = verify_account(username, password)
        return redirect(url_for(endpoint=endpoint, message=message))
    return render_template("signin.html")

def verify_account(username, password):
    if username == "" or password == "":
        return ("error", "請輸入帳號、密碼")
    elif username == "test" and  password == "test":
        session["signin_state"] = 1
        return ("member", None)
    else:
        return ("error", "帳號、或密碼輸入錯誤")

@app.route("/signout/", methods=['GET'])
def signout():
    session["signin_state"] = 0
    return redirect("/")

@app.route("/member/", methods=['GET'])
def member():
    if "signin_state" in session:
        if session["signin_state"] == 1:
            return render_template("member.html")
    return redirect("/")

@app.route("/error/", methods=['GET'])
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)

if __name__ == '__main__':
    app.run(debug=True, port=3000)