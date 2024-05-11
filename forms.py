from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#Nombres: Gael Humberto Borchardt Castellanos Daniel Ivan Estrada Neri
class SearchForm(FlaskForm):
    search = StringField('Search...', validators=[DataRequired()])
    submit = SubmitField('Search')