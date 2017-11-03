import bson.json_util
import json
from mongoengine import StringField, IntField, DateTimeField, ListField
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models import Common
from configs.DevConfig import SECRET_KEY


class User(Common):
    user_id = StringField(max_length=64)
    name = StringField(max_length=32)
    age = IntField(max_value=130, min_value=10)
    avatar = StringField(max_length=128)
    nickname = StringField(max_length=32)
    # 用户等级
    level = IntField()
    # 手机号码 到时候要发送短信用
    phone = StringField(max_length=64)
    birthday = DateTimeField()
    timestamp = StringField()
    # 密码的hash值
    password_hash = StringField(max_length=128)
    # 粉丝
    followers = ListField(StringField())
    followers_num = IntField(default=0)
    # 关注的人
    idol = ListField(StringField())
    idol_num = IntField(default=0)

    def set_id(self):
        '''
        重写父类函数
        :return: void
        '''
        i = ''
        ids = json.loads(bson.json_util.dumps(self.pk))
        for name, value in ids.items():
            i = value
        self.update(user_id=i)

    def set_save(self):
        '''
        重写父类函数
        :return: void
        '''
        self.save()
        self.set_id()

    # 添加跟随者
    def add_follower(self, obj_id):
        self.followers.append(obj_id)
        self.followers_num = int(self.followers_num) + 1
        self.save()

    # 删除跟随者
    def delete_follower(self, obj_id):
        self.update(pull__followers=obj_id)
        self.followers_num = int(self.followers_num) - 1
        self.save()
        self.reload()

    # 添加偶像
    def add_idol(self, obj_id):
        self.idol.append(obj_id)
        self.idol_num = self.idol_num + 1
        self.save()

    # 删除偶像
    def delete_idol(self, obj_id):
        self.update(pull__idol=obj_id)
        self.idol_num = int(self.idol_num) - 1
        self.save()
        self.reload()

    # 生成token
    def generate_token(self):
        s = Serializer(SECRET_KEY)
        return s.dumps({'token': self.user_id})

    # 检查token
    def check_token(self, token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except:
            return False
        if data['token'] != self.user_id:
            return False
        else:
            return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.save()

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
