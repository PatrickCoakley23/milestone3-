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
    meal_type = mongo.db.recipe_categories.find())

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes

    enter_recipes = {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_category': request.form.get('meal_type'),
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
        'permission_to_delete': True
    }
    
    
    recipes.insert_one(enter_recipes)
    return redirect(url_for("get_recipes"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
