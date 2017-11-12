from flask import jsonify, request, g

from app.api_1_0 import api
from app.forms.circle import CircleWordForm
from app.models import PostCommon


@api.route('/circle/word/<int:id>', methods=['GET', 'DELETE'])
def get_delete_circle_word(obj_id):
    '''
    得到这个circle的json数据 以及删除这个 circle
    :param obj_id: circle的id
    :return:
    '''
    circle = PostCommon.objects(id=obj_id).first()

    if request.method == "GET":

        if circle is None:
            return jsonify({
                'status': 400,
                'des': '找不到该信息'
            })
        else:
            return jsonify({
                'status': 200,
                'des': '成功',
                'data': circle.get_json()
            })
    elif request.method == "DELETE":

        if circle is None:
            return jsonify({
                'status': 404,
                'des': '未找到'
            })
        if g.user == circle.author:
            circle.delete()
            return jsonify({
                'status': 200,
                'des': '删除成功'
            })
        else:
            return jsonify({
                'status': 400,
                'des': '没有权限'
            })


@api.route('/circle/words/', methods=['POST'])
def insert_circle():
    '''
    如果是设置隐私的：
        推送到私密post的集合之中
        推送给自己的好友
    如果设置自己的：
        也是推送到自己的post集合之中
    如果是公开的:
        直接设置是公开的就行不需要推送
    好友获取post的时候
        获取公开的 以及私密的
    :return:
    '''
    form = CircleWordForm()
    if form.validate_on_submit():
        circle = PostCommon()
        circle.title = form.title.data
        circle.content = form.content.data
        circle.permission = request.values.get('permission')
        # 进行分类管理 还没有具体实现怎么分配
        if circle.permission == 1:
            print("1")
        elif circle.permission == 2:
            print("2")
        elif circle.permission == -1:
            print("-1")
        else:
            print("else")
        circle.author = g.user
        circle.set_save()
        return jsonify({
            'status': 200,
            'des': '新建成功',
            'data': circle.get_json()
        })
    else:
        return jsonify({
            'status': 400,
            'des': '新建失败'
        })


# 测试应用区

@api.route('/circle/word/', methods=['DELETE'])
def del_all_word():
    word = PostCommon.objects.all()
    word.delete()
    return 'ok'
