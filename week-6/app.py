from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mysqlConnector import account_query, account_create

app = Flask(__name__)

app.secret_key = "jf8932fhuewifnd9o"

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/signin/", methods=['POST'])
def signin():
    query_username = None
    query_password = None
    username = request.form["username"]
    password = request.form["password"]
    if account_query(username): 
        query_username = account_query(username)['username']
        query_password = account_query(username)['password']
    if username == "" or password == "":
        return redirect(url_for('error', message="請輸入帳號、密碼"))
    elif check_password_hash(query_password, password):
        session["signin_member"] = query_username
        return redirect(url_for("member"))
    else:
        return redirect(url_for('error', message="帳號、或密碼輸入錯誤"))
    
@app.route("/signup/", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        hashed_password = generate_password_hash(request.form["password"])
        if account_query(username):
            return redirect(url_for('error', message="帳號已被註冊"))
        else:
            account_create(name, username, hashed_password)
            return redirect("/")
    return render_template("signup.html")

@app.route("/signout/", methods=['GET'])
def signout():
    session.pop('signin_member', None)
    return redirect("/")

@app.route("/member/", methods=['GET'])
def member():
    if "signin_member" in session:
        name = account_query(session["signin_member"])['name']
        return render_template("member.html", message = name)
    return redirect("/")

@app.route("/error/", methods=['GET'])
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)

if __name__ == '__main__':
    app.run(debug=True, port=3000)