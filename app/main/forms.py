from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField

class PitchForm1(FlaskForm):
    content = TextAreaField('New Pitch')
    category= SelectField('pi')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    category_id = SelectField('Pitch Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    comment_section_id = TextAreaField('New Comment')
    submit = SubmitField('Submit')
