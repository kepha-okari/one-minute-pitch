from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField

class PitchForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    # category_id = SelectField('Pitch Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')
