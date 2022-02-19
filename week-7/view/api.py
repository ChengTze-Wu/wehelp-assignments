from flask import Blueprint, request, Response
from mysqlConnector import account_query, account_name_update
from flask import session
import json

api = Blueprint('api', __name__)

@api.route("/members/", methods=['GET'])
def get_member_json():
    username = request.args.get("username")
    if account_query(username):
        id, name, username = map(account_query(username).get, ('id', 'name', 'username'))
        result = json.dumps({"data":{"id":id, "name":name, "username":username}}, ensure_ascii=False)
    else:
        result = json.dumps({"data":None})
    resp = Response(result)
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    return resp

@api.route("/member/", methods=['POST'])
def update_name():
    request_json = request.get_data()
    name = json.loads(request_json)["name"]
    if "signin_member" in session:
        account_name_update(name, session["signin_member"])
        result = json.dumps({"ok":True})
    else:
        result = json.dumps({"error":True})
    resp = Response(result)
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    return resp
