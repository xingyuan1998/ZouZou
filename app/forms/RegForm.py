from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class RegForm(FlaskForm):
    phone = StringField(
        'phone',
        validators=[DataRequired()]
    )
    name = StringField(
        'name',
        validators=[DataRequired()]
    )
    password = StringField(
        'password',
        validators=[DataRequired()]
    )
    code = StringField(
        'code',
        validators=[DataRequired()]
    )


