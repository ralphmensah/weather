from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NewForm(FlaskForm):
    location = StringField(validators=[DataRequired()])
    submit = SubmitField("Search")