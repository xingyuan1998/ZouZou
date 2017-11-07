from mongoengine import ListField, StringField, IntField

from app.models import Common, PostCommon


class CircleImage(PostCommon):
    images = ListField(StringField(max_length=64))
    images_num = IntField()


class CircleVideo(PostCommon):
    video = StringField(max_length=64)
    video_size = StringField()
