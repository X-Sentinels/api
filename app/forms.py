from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField
from wtforms.validators import DataRequired,Length


class LoginForm(FlaskForm):
    username = StringField(
        validators=[DataRequired("Please input your username"),Length(1,64)],
        render_kw={
            "class": "form-control",
            "placeholder": "username",
            "required": "required"
        }
    )
    password = PasswordField(
        validators=[DataRequired("Please input your password")],
        render_kw={
            "class": "form-control",
            "placeholder": "password",
            "required": "required"
        }
    )
    remember_me = BooleanField(
        'Keep me logged in',
        render_kw={
            "class":"main-checkbox"
        }
    )
    submit = SubmitField(
        'Log In',
        render_kw={
        "class": "btn btn-default"
    }
    )


class CurlForm(FlaskForm):
    args_ipversion = SelectField(
        label='ipversion',
        validators=[DataRequired()],
        choices=[('0', 'ipv4'), ('1', 'ipv6')],
         render_kw={
            "class": "form-control"
        }
    )
    args_url = StringField(
        label='url',
        validators = [DataRequired("Please input your url"),Length(1,64)],
        render_kw = {
        "class": "form-control"
    }
    )

    args_timeout = StringField(
        label='timeout',
        validators=[DataRequired("Please input your url_timeout"), Length(1, 64)],
        render_kw={
            "class": "form-control"
        }
    )
    submit_curl= SubmitField(
        'Submit',
        render_kw={
            "class": "btn btn-default"
        }
    )


class PingForm(FlaskForm):
    args_ipversion = SelectField(
        label='ipversion',
        validators=[DataRequired()],
        choices=[('0', 'ipv4'), ('1', 'ipv6')],
        render_kw={
            "class": "form-control"
        }
    )
    args_url = StringField(
        label='url',
        validators = [DataRequired("Please input your url"),Length(1,64)],
        render_kw = {
        "class": "form-control"
    }
    )
    args_packagesize = StringField(
        label='packetagesize',
        validators=[DataRequired("Please input your packagesize"), Length(1, 64)],
        render_kw={
            "class": "form-control"
        }
    )
    args_count = StringField(
        label='count',
        validators=[DataRequired("Please input your count"), Length(1, 64)],
        render_kw={
            "class": "form-control"
        }
    )

    args_timeout = StringField(
        label='timeout',
        validators=[DataRequired("Please input your timeout"), Length(1, 64)],
        render_kw={
            "class": "form-control"
        }
    )
    submit_ping= SubmitField(
        'Submit',
        render_kw={
            "class": "btn btn-default"
        }
    )
