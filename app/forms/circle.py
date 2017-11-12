from flask_wtf import FlaskForm
from mongoengine import IntField
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CircleWordForm(FlaskForm):
    title = StringField(
        'title',
        validators=[DataRequired()]
    )
    content = StringField(
        'content',
        validators=[DataRequired()]
    )
    permission = IntField(
        'permission',
        validators=[DataRequired()]
    )
