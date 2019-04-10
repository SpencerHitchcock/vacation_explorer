from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class SearchForm(FlaskForm):
    vacation_start = DateField('Start Date', format='%Y-%m-%d')
    vacation_end = DateField('End Date', format='%Y-%m-%d')
    search = SubmitField('Search')