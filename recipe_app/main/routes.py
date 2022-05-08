from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from recipe_app.models import User, Recipe, Collection
from recipe_app.main.forms import RecipeForm, CollectionForm


main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    collections = Collection.query.all()
    print(collections)
    return render_template('home.html', collections=collections)

