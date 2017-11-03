import datetime

from flask import Blueprint, jsonify

from app.models.user import User

api = Blueprint('api', __name__, url_prefix='/api')

from app.api_1_0 import user


@api.route('/')
def hello():
    # user = User()
    # user.name = 'sdfdsf'
    # user.age = 12
    # user.timestamp = str(datetime.datetime.now())
    # user.set_save()
    users = User.objects.first()
    # 检测token是否可用
    # return jsonify({
    #     'status': 200,
    #     'token': str(str(users.generate_token())[2:-1])
    # })
    # return jsonify({
    #     'status': 200,
    #     'token': users.check_token(
    #         "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUwOTcwNDE4NSwiZXhwIjoxNTA5NzA3Nzg1fQ.eyJ0b2tlbiI6IjU5ZmJmNDEyZDIyNDk4MDAyMDBlY2QwZiJ9.Gw4EL3JPyRsZWxRh6upk2IZW2SciTtbzd7ZGqdp_GLg")
    # })

    # users.add_follower("ddsfsdfsfasdf")
    users.update(pull__followers="ddsfsdfsfasdf")
    users.followers_num = int(users.followers_num) - 1
    users.save()
    users.reload()
    return jsonify(users)


@api.route('/del/')
def delete():
    user = User.objects.all()
    user.delete()
    return 'delete ok'
