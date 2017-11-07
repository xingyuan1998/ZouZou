from flask import Blueprint, jsonify, session, request, g
import datetime
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serialozer

api = Blueprint('api', __name__, url_prefix='/api')
from app.api_1_0 import user
from app.api_1_0 import circleword

@api.before_request
def bef_request():
    '''
    api 请求之前 验证token 和 手机号是否是同一个人
    是一个人才能继续进行并把user 放到 g 上
    :return:
    '''
    token = request.values.get('token')
    phone = request.values.get('phone')
    if token is None:
        return jsonify({
            'status': 400,
            'des': "token为空"
        })
    user = User.objects(phone=phone).first()
    if user is None:
        return jsonify({
            'status': 400,
            'des': '该用户不存在'
        })
    if user.check_token(token):
        g.user = user
    else:
        return jsonify({
            'status': 400,
            'des': '登录失效，请重新登录'
        })


@api.route('/')
def hello():
    # user = User()
    # user.name = 'sdfdsf'
    # user.age = 12
    # user.timestamp = str(datetime.datetime.now())
    # user.set_save()
    users = User.objects.all()
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

    # # users.add_follower("ddsfsdfsfasdf")
    # # users.update(pull__followers=)
    # # users.followers_num = int(users.followers_num) - 1
    # # users.delete_follower("ddsfsdfsfasdf")
    # users.save()
    # users.reload()
    return jsonify(users)


@api.route('/del/')
def delete():
    user = User.objects.all()
    user.delete()
    return 'delete ok'


@api.route('/show/')
def show():
    user = User.objects.all()
    return jsonify(user)
