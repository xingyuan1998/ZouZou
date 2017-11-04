from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class FindPwdForm(FlaskForm):
    phone = StringField(
        'phone',
        validators=[DataRequired()]
    )


class ChangePwdForm(FlaskForm):
    phone = StringField(
        'phone',
        validators=[DataRequired()]
    )
    password = StringField(
        'password',
        validators=[DataRequired()]
    )
