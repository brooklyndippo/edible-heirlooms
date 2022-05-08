from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, TextAreaField, IntegerField, DateField, SelectField, SubmitField, FloatField, PasswordField, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from recipe_app.models import RecipeCategory, User, Recipe, Collection

class CollectionForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField(label='Title')
    description = StringField(label='Description')

def get_choices():
    return RecipeCategory.choices()

class RecipeForm(FlaskForm):
    """Form for adding/updating a Recipe."""
    title = StringField(label='Title')
    author = StringField(label='Author')
    origin_story = TextAreaField(label='Origin Story')
    category = SelectField(label='Category', choices=get_choices())
    image = StringField(label='Image URL')
    serving_size = IntegerField(label='Serves')
    ingredients = TextAreaField(label='Ingredients')
    preparation = TextAreaField(label='Preparation')
