from flask import jsonify

from app.api_1_0 import api
from app.models.user import User


# 得到某个用户的信息
@api.route('/user/<string:id>/')
def get_user_info(id):
    user = User.objects(user_id=id).only('name', 'user_id', 'age').first()
    if user is None:
        return jsonify({
            'status': 404,
            'des': '没有找到该用户'
        })
    return jsonify({
        'status': 200,
        'data': user
    })


