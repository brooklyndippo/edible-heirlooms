from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from recipe_app.models import User, Recipe, Collection
from recipe_app.main.forms import RecipeForm, CollectionForm
from recipe_app.extensions import db
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    collections = Collection.query.all()
    print(collections)
    return render_template('home.html', collections=collections)


# ======== COLLECTIONS ========= NEW/CREATE =========

@main.route('/new_collection', methods=['GET', 'POST'])
def new_collection():
    form = CollectionForm()

    if form.validate_on_submit(): 
        collection = CollectionForm(
            title = form.title.data,
            description = form.description.data,
            curated_by=current_user
        )
        db.session.add(collection)
        db.session.commit()
        flash('Succes! You created a new collection.')
        
        return redirect(url_for('main.show_collection', collection_id=collection.id))

    return render_template('new_collection.html', form=form, form_title='New Collection')

# ======== COLLECTIONS ========= SHOW/UPDATE =========

@main.route('/collection/<collection_id>', methods=['GET', 'POST'])
def show_collection(collection_id):
    collection = Collection.query.get(collection_id)
    form = CollectionForm(obj=collection)

    if form.validate_on_submit():
        collection.title = form.title.data
        collection.description = form.description.data

        db.session.commit()
        flash('Collection Updated.')
        return redirect(url_for('main.show_collection', collection_id=collection_id))

    return render_template('show_collection.html', form=form, form_title='Edit Collection', collection=collection)



# ======== RECIPES ========= NEW/CREATE =========

@main.route('/new_recipe', methods=['GET', 'POST'])
def new_recipe():
    
    form = RecipeForm()

    if form.validate_on_submit(): 
        recipe = Recipe(
            title = form.title.data,
            author = form.author.data,
            origin_story = form.origin_story.data,
            image = form.image.data,
            category = form.category.data,
            serving_size = form.serving_size.data,
            ingredients = form.ingredients.data,
            preparation = form.preparation.data,
            shared_by=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Succes! You created a new recipe.')
        
        return redirect(url_for('main.show_recipe', recipe_id=recipe.id))

    return render_template('new_recipe.html', form=form, form_title='New Recipe')

# ======== RECIPES ========= SHOW/UPDATE =========

@main.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def show_recipe(recipe_id):
    recipe = Collection.query.get(recipe_id)
    form = CollectionForm(obj=recipe)

    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.author = form.author.data
        recipe.origin_story = form.origin_story.data
        recipe.image = form.image.data
        recipe.category = form.category.data
        recipe.serving_size = form.serving_size.data
        recipe.ingredients = form.ingredients.data
        recipe.preparation = form.preparation.data

        db.session.commit()
        flash('Recipe Updated.')
        return redirect(url_for('main.show_recipe', recipe_id=recipe_id))

    return render_template('show_recipe.html', form=form, form_title='Edit Recipe', recipe=recipe)
