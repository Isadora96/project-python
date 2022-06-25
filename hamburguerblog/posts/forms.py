from ast import Sub
from flask_wtf import FlaskForm
from sqlalchemy import DATE
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField("Post"
    )