from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FloatField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length, Optional
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_babel import _, lazy_gettext as _l
from app.models import User
from datetime import date
from flask import url_for


class LoginForm(FlaskForm):
    username = StringField(_l('Benutzername'), validators=[DataRequired()])
    password = PasswordField(_l('Passwort'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Anmelden'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Benutzername'), validators=[DataRequired()])
    email = StringField(_l('E-Mail'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Passwort'), validators=[DataRequired()])
    password2 = PasswordField(_l('Passwort wiederholen'), 
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Registrieren'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Bitte verwende einen anderen Benutzername.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Bitte verwende eine andere E-Mail Addresse.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('E-Mail'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Passwort zurücksetzten'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Passwort'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Passwort wiederholen'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Passwort zurücksetzten'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Benutzername'), validators=[DataRequired()])
    about_me = TextAreaField(_l('Über mich'), validators=[Length(min=0, max=140)])
    email = StringField(_l('E-Mail'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Übermitteln'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Bitte verwende einen anderen Benutzernamen.'))
   
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Bitte verwende eine andere E-Mail Addresse.'))

class EmptyForm(FlaskForm):
    submit = SubmitField('Übermitteln')

##########################
# Eigens erstellter Code #
##########################

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    description = StringField('Description')
    private = BooleanField('Private Event')
    submit = SubmitField('Create Event')
