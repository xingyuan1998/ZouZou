from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    phone = StringField(
        'phone',
        validators=[DataRequired()]
    )
    password = StringField(
        'password',
        validators=[DataRequired()]
    )
