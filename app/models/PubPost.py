from mongoengine import StringField, ReferenceField, Document

from app.models import User


class PubPost(Document):
    post_id = StringField(max_length=128)
    user = ReferenceField(User)
    timestamp = StringField(max_length=64)
