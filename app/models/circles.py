from mongoengine import ListField, StringField, IntField, ReferenceField

from app.models import Common, PostCommon


class CircleImage(PostCommon):
    images = ListField(StringField(max_length=64))
    images_num = IntField()


class CircleVideo(PostCommon):
    video = StringField(max_length=64)
    video_size = StringField()


class SelfPost(Common):
    # 1 为文字 2 为 图片 3 为视频
    type = IntField()
    post = ReferenceField()
