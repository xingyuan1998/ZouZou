from mongoengine import StringField, ReferenceField, Document

from app.models import User


class PubPost(Document):
    post_id = StringField(max_length=128)
    user = ReferenceField(User)
    timestamp = StringField(max_length=64)

    @staticmethod
    def del_post(obj_id):
        post = PubPost.objects(obj_id).first()
        if post is None:
            return_json = {
                'status': 404,
                'des': '未找到这个'
            }
            return return_json
        post.delete()
        return_json = {
            'status': 404,
            'des': '删除成功'
        }
        return return_json
