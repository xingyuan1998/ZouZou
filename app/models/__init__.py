import datetime

from flask_mongoengine import Document
from mongoengine import StringField, ListField, ReferenceField, IntField, BooleanField
import json
import bson.json_util

from app.models.user import User


class Common(Document):
    d_id = StringField(max_length=64)
    timestamp = StringField()
    meta = {'allow_inheritance': True}

    def set_id(self):
        i = ''
        ids = json.loads(bson.json_util.dumps(self.pk))
        for name, value in ids.items():
            i = value
        self.update(d_id=i)

    def set_save(self):
        self.timestamp = str(datetime.datetime.now())
        self.save()
        self.set_id()
        self.reload()

class Comment(Common):
    author = ReferenceField(User)
    title = StringField(max_length=128)
    content = StringField()
    # 是否是一个回复
    is_reply = BooleanField(default=False)
    # 上个评论的id
    last_Comment = StringField(max_length=32)
    # 上个评论的内容
    last_Comment_content = StringField()
    # 上个评论的作者
    last_Comment_author = ReferenceField(User)

    meta = {'allow_inheritance': True}

    def get_json(self):
        if self.is_reply:
            json_obj = {
                'id': self.d_id,
                'title': self.title,
                'content': self.content,
                'author_id': self.author.user_id,
                'author_name': self.author.name,
                'is_reply': True,
                'last_comment': self.last_Comment,
                'last_comment_content': self.last_Comment_content,
                'last_comment_author': self.last_Comment_author.user_id,
                'last_comment_author_name': self.last_Comment_author.name
            }
        else:
            json_obj = {
                'id': self.d_id,
                'title': self.title,
                'content': self.content,
                'author_id': self.author.user_id,
                'author_name': self.author.name,
            }
        return json_obj


class PostCommon(Common):
    title = StringField(max_length=128)
    content = StringField()
    author = ReferenceField(User)
    hot = IntField(default=0)
    good = IntField(default=0)
    comments = ListField(ReferenceField(Comment))
    timestamp = StringField()
    # 权限 分配 是否是自己可看 朋友可看 还是全部人可见
    # -1 自己可见  1 朋友可见 2 全部人课件
    permission = IntField()

    meta = {'allow_inheritance': True}

    def get_json(self):
        com = []
        if self.comments is None or len(self.comments) == 0:
            com = []
        else:
            for comment in self.comments:
                com.append(comment.get_json())
        json_obj = {
            'id': self.d_id,
            'title': self.title,
            'content': self.content,
            'author_id': self.author.user_id,
            'author_name': self.author.name,
            'hot': self.hot,
            'good': self.good,
            'comments': com,
            'timestamp': self.timestamp,
            'permission': self.permission
        }
        return json_obj
