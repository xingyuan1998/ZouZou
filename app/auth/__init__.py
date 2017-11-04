import datetime
import random

from flask import Blueprint, jsonify, request, session

from app.forms.FindPwdForm import FindPwdForm, ChangePwdForm
from app.forms.LoginForm import LoginForm
from app.forms.RegForm import RegForm
from app.models.user import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/reg/phone/', methods=['POST'])
def send_phone_message():
    '''
    注册 给用户发个短信
    :return:
    '''
    phone = request.values.get('phone')
    user = User.objects(phone=phone).first()
    if user is not None:
        return jsonify({
            'status': 400,
            'des': '用户已经注册了'
        })
    session[phone] = random.randint(1000, 9999)
    session['last_reg_time'] = datetime.datetime.time()
    return str(session[phone])


@auth.route('/reg/', methods=['POST'])
def reg():
    '''
    先检测code是否正确，正确则继续 否则返回失败
    :return:
    '''
    form = RegForm()
    if form.validate_on_submit():
        code = form.code.data
        phone = form.phone.data
        if phone in session and str(session[phone]) == code:
            form = RegForm()
            if form.validate_on_submit():
                user = User()
                user.phone = phone
                user.name = form.name.data
                user.set_password(form.password.data)
                user.set_save()
                return jsonify({
                    'status': 200,
                    'data': user
                })
            return jsonify({
                'status': 400,
                'des': '注册成功'
            })
        return jsonify({
            'status': 400,
            'des': 'code错误'
        })


@auth.route('/login/', methods=['POST'])
def login():
    '''
    用户登陆 使用手机号和密码
    :return:
    '''
    form = LoginForm()
    if form.validate_on_submit():
        phone = form.phone.data
        password = form.password.data
        user = User.objects(phone=phone).first()
        if user is None:
            return jsonify({
                'status': 400,
                'des': '该用户不存在'
            })
        if user.verify_password(password=password):
            return jsonify({
                'status': 200,
                'des': '登陆成功',
                'token': str(str(user.generate_token())[2:-1])
            })


@auth.route('/find/password/', methods=['POST'])
def find_pwd():
    '''
    找回密码 发送短信验证码
    :return:
    '''
    form = FindPwdForm()
    if form.validate_on_submit():
        phone = form.phone.data
        session['find_' + phone] = random.randint(1000, 9999)
        session['last_find_time'] = datetime.datetime.time()
        return str(session['find_' + +'phone'])
    return jsonify({
        'status': 400,
        'des': '手机号错误'
    })


@auth.route('/change/password/', methods=['POST'])
def change_pwd():
    '''
    验证短信验证码
    :return:
    '''
    form = ChangePwdForm()
    if form.validate_on_submit():
        phone = form.phone.data
        password = form.password.data
        user = User.objects(phone=phone).first()
        if user is None:
            return jsonify({
                'status': 404,
                'des': '未找到该用户'
            })
        user.set_password(password)
        user.save()
        return jsonify({
            'status': 200,
            'des': '密码修改成功',
            'token': str(str(user.generate_token())[2:-1])
        })
    return jsonify({
        'status': 400,
        'des': '修改密码失败'
    })
