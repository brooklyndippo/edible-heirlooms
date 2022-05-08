from sqlalchemy import table
from sqlalchemy_utils import URLType
from flask_login import UserMixin
from recipe_app.extensions import db
from recipe_app.utils import FormEnum

class RecipeCategory(FormEnum):
    """Categories of grocery items."""
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DESSERT = 'Dessert'
    HOLIDAY = 'Holiday'
    OTHER = 'Other'


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    origin_story = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.Enum(RecipeCategory), default=RecipeCategory.OTHER)
    serving_size = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    preparation = db.Column(db.String(3000), nullable=False)
    collections = db.relationship('Collection', secondary='recipe_collection', back_populates='recipes')
    shared_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    sharer = db.relationship('User')

recipe_collections = db.Table('recipe_collection',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('collection_id', db.Integer, db.ForeignKey('collection.id'))
)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    recipes = db.relationship('Recipe', secondary='recipe_collection', back_populates='collections')
    curated_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    curator = db.relationship('User')
    
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20), nullable=False, unique=True)
    password = db.Column (db.String(20), nullable=False)
    first_name = db.Column (db.String(20), nullable=False)
    last_name = db.Column (db.String(20), nullable=False)

# user_recipes = db.Table('user_recipe',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
# )

# user_collections = db.Table('user_collection',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('collection_id', db.Integer, db.ForeignKey('collection.id'))
# )