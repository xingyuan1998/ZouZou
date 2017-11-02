import bson.json_util
import json
from mongoengine import StringField, IntField, DateTimeField, ListField

from exts import db
from flask_mongoengine import Document


class User(Document):
    user_id = StringField(max_length=64)
    name = StringField(max_length=32)
    age = IntField(max_value=130, min_value=10)
    avatar = StringField(max_length=128)
    nickname = StringField(max_length=32)
    level = IntField()
    birthday = DateTimeField()
    timestamp = StringField()
    # 粉丝
    followers = ListField(StringField())
    # 关注的人
    idol = ListField(StringField())

    def set_id(self):
        i = ''
        ids = json.loads(bson.json_util.dumps(self.pk))
        for name, value in ids.items():
            i = value
        self.update(user_id=i)

    def set_save(self):
        self.set_id()
