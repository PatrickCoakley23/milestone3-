import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'milestone3'
app.config["MONGO_URI"] = os.environ['MONGO_URI']


mongo = PyMongo(app)


@app.route('/')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipes.html',
    recipe_categories = mongo.db.recipe_categories.find())


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    

    enter_recipes = {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_category': request.form.get('recipe_category'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'calories': request.form.get('calories'),
        'protein': request.form.get('protein'),
        'carbs': request.form.get('carbs'),
        'fat': request.form.get('fat'),
        'servings': request.form.get('servings'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'image_link': request.form.get('image_link'),
        'description': request.form.get('description'),
        'permission_to_delete': True
    }
       
    recipes.insert_one(enter_recipes)
    return redirect(url_for("get_recipes"))


@app.route('/recipe_selected/<recipe_id>')
def recipe_selected(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template('recipe_selected.html', recipes=the_recipe,)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.recipe_categories.find()
    return render_template('edit_recipe.html', recipe=recipe, 
                            categories=categories)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_category': request.form.get('recipe_category'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'calories': request.form.get('calories'),
        'protein': request.form.get('protein'),
        'carbs': request.form.get('carbs'),
        'fat': request.form.get('fat'),
        'servings': request.form.get('servings'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'image_link': request.form.get('image_link'),
        'description': request.form.get('description')
    })   
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
