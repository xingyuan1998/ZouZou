import datetime

from flask import Blueprint, jsonify

from app.models.user import User

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def hello():
    user = User()
    user.name = 'sdfdsf'
    user.age = 12
    user.timestamp = str(datetime.datetime.now())
    user.save()
    user.set_id()
    users = User.objects.all()
    return jsonify(users)


@api.route('/del/')
def delete():
    user = User.objects.all()
    user.delete()
    return 'delete ok'
