import os
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_parameter
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SECRET_KEY'] = os.environ['secret_key']
app.config["MONGO_DBNAME"] = 'milestone3'
app.config["MONGO_URI"] = os.environ['MONGO_URI']


mongo = PyMongo(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index(): 
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.check_password_hash(login_user['password'], request.form.get('pass')):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form.get('username')})

        if existing_user is None:
            password = request.form.get("pass")
            hashpass = bcrypt.generate_password_hash(password).decode('utf-8')
            users.insert({'name' : request.form.get('username'), 'password' : hashpass})
            session['username'] = request.form.get('username')
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')



@app.route('/recipes')
def get_recipes():
    per_page = 9
    recipes = mongo.db.recipes.find()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    skips = per_page * (page - 1)
    cursor = recipes.skip(skips).limit(per_page)
    pagination = Pagination(page=page, total=recipes.count(), record_name='recipes', per_page=per_page, bs_version=4, css_framework='bootstrap', alignment='center')
    return render_template("recipes.html", recipes=recipes, pagination=pagination)




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
        'description': request.form.get('description'),
        'permission_to_delete': True
    })   
    flash('recipe has been edited')
    return redirect(url_for('get_recipes'))
    

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash('recipe has been deleted')
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True),
          
