"""
 Flask REST application

"""

from flask import Flask, request, jsonify, make_response
import db

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/api/users/", methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        # return all users
        users = db.get_users()
        return make_response(jsonify(users))
    elif request.method == 'POST':
        # add a user
        user = request.get_json()
        user = db.add_user(user)
        return make_response(jsonify(user, 201))


@app.route("/api/user/<int:pk>", methods=['GET', 'DELETE', 'PUT'])
def single_user(pk):
    user = db.get_user(pk)
    if user is None:
        return make_response((jsonify(), 404))
    if request.method == 'GET':
        return make_response(jsonify(user))
    elif request.method == 'DELETE':
        db.remove_user(user)
        return make_response(jsonify(), 200)
    elif request.method == 'PUT':
        user = request.get_json()
        db.update_user(pk, user)
        user = db.get_user(pk)
        return make_response(jsonify(user))


db.recreate_db()
app.run(host='0.0.0.0', port=8000, debug=True)
