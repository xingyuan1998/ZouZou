from flask_mongoengine import Document
from mongoengine import StringField
import json
import bson.json_util


class Common(Document):
    d_id = StringField(max_length=64)
    meta = {'allow_inheritance': True}

    def set_id(self):
        i = ''
        ids = json.loads(bson.json_util.dumps(self.pk))
        for name, value in ids.items():
            i = value
        self.update(d_id=i)

    def set_save(self):
        self.save()
        self.set_id()
