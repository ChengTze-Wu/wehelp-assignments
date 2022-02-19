from flask import Blueprint, request
from flask import render_template
from flask import session
from flask import request
from flask import redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from mysqlConnector import account_query, account_create

auth = Blueprint('auth', __name__)

@auth.route('/', methods=["GET"])
@auth.route("/signin/", methods=['POST'])
def signin():
    if request.method == "POST":
        query_username = ""
        query_password = ""
        username = request.form["username"]
        password = request.form["password"]
        if account_query(username):
            query_username, query_password = map(account_query(username).get, ('username', 'password'))
        if username == "" or password == "":
            return redirect(url_for('auth.error', message="請輸入帳號、密碼"))
        elif check_password_hash(query_password, password):
            session["signin_member"] = query_username
            return redirect(url_for("auth.member"))
        else:
            return redirect(url_for('auth.error', message="帳號、或密碼輸入錯誤"))
    return render_template("auth/signin.html")

@auth.route("/signup/", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        hashed_password = generate_password_hash(request.form["password"])
        if account_query(username):
            return redirect(url_for('auth.error', message="帳號已被註冊"))
        else:
            account_create(name, username, hashed_password)
            return redirect("/")
    return render_template("auth/signup.html")

@auth.route("/signout/", methods=['GET'])
def signout():
    session.pop('signin_member', None)
    return redirect("/")

@auth.route("/member/", methods=['GET'])
def member():
    if "signin_member" in session:
        name = account_query(session["signin_member"])['name']
        return render_template("auth/member.html", message = name)
    return redirect("/")

@auth.route("/error/", methods=['GET'])
def error():
    message = request.args.get("message")
    return render_template("auth/error.html", message=message)