import os
from flask import (
    Flask, render_template, url_for,
    request, redirect, flash, session
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_parameter
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config["MONGO_DBNAME"] = os.environ['MONGO_DBNAME']
app.config["MONGO_URI"] = os.environ['MONGO_URI']


mongo = PyMongo(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/login')
def login():
    """
    If statement. Users who are already logged in are
    redirected to  to 'my recipes' page.
    """
    if 'username' in session:
        flash('You are logged in as ' + session['username'])
        return redirect(url_for('my_recipes'))
    return render_template('login.html')


@app.route('/update', methods=['POST', 'GET'])
def update_login():
    users = mongo.db.users
    password = request.form.get('pass')
    login_user = users.find_one({'username': request.form['username']})
    """
    Users either input correct login details and gain access to the page.
    Otherwise they are greeted with the Flash message:
    "Invalid username/password combination"
    """
    if login_user:
        if bcrypt.check_password_hash(login_user['password'], password):
            session['username'] = request.form['username']
            flash('You Have Successfully Logged In ' + session['username'])
            return redirect(url_for('my_recipes'))
    flash('Invalid username/password combination')
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    New users who enter username that is already used in database,
    they'll be greeted with the flash message;
    "That username already exists!"
    Otherwise they can register an account.
    """
    flash('Create An Account For Free To Add Your Own Recipes')
    if request.method == 'POST':
        users = mongo.db.users
        username = request.form.get('username')
        existing_user = users.find_one({'username': username})

        if existing_user is None:
            password = request.form.get("pass")
            username = request.form.get('username')
            fullname = request.form.get('fullname')
            email = request.form.get('email')
            hashpass = bcrypt.generate_password_hash(password).decode('utf-8')
            users.insert({
                'username': username,
                'password': hashpass,
                'fullname': fullname,
                'email': email
            })

            session['username'] = request.form.get('username')
            flash(
                'Hello ' + session['username'] +
                ' Welcome to Patrick Coakley Nutrition'
            )
            return redirect(url_for('get_recipes'))
        flash('That username already exists!')
    return render_template('register.html')


# Hero Image
@app.route('/')
def homepage():
    """
    checks if user is logged in. 
    if not logged in displays flash 
    message. 
    """
    if 'username' in session:
        return render_template('hero_image.html')
    flash('Create An Account For Free To Add Your Own Recipes')
    return render_template('hero_image.html')
 

@app.route('/recipes')
def get_recipes():
    """
    Recipes page. Use pagination here. Need skip function
    to ignore the previous page's content when going to
    next page.
    """
    per_page = 9
    recipes = mongo.db.recipes.find()
    recipe_categories = mongo.db.recipe_categories.find()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    skips = per_page * (page - 1)
    cursor = recipes.skip(skips).limit(per_page)
    pagination = Pagination(
        page=page, total=recipes.count(),
        record_name='recipes', per_page=per_page,
        bs_version=4, css_framework='bootstrap',
        alignment='center'
        )
    return render_template(
        "recipes.html", recipes=recipes,
        pagination=pagination,
        recipe_categories=recipe_categories
        )


@app.route('/recipe_type/<recipe_type>')
def recipe_category(recipe_type):
    """
    Used for the dropdown menu for filtering.
    Functionality same as recipes page, just
    categories are iterated in a for loop to give
    each dropdown item a different href
    """
    per_page = 9
    recipes = mongo.db.recipes.find({'recipe_category': recipe_type})
    recipe_categories = mongo.db.recipe_categories.find()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    skips = per_page * (page - 1)
    cursor = recipes.skip(skips).limit(per_page)
    pagination = Pagination(
        page=page, total=recipes.count(),
        record_name='recipes', per_page=per_page,
        bs_version=4, css_framework='bootstrap',
        alignment='center'
        )
    return render_template(
        "recipes.html", recipes=recipes,
        recipe_categories=recipe_categories,
        pagination=pagination
        )


@app.route('/add_recipe')
def add_recipe():
    """
    Checks if user is in session as login
    is required for adding recipes.
    """
    if 'username' in session:
        categories = mongo.db.recipe_categories.find()
        return render_template(
            'add_recipes.html',
            recipe_categories=categories
            )
    return redirect(url_for('access_denied'))


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    """
    session[username] is inputted as a value so i can
    filter recipes by username for 'My Recipes"
    """
    if 'username' in session:
        recipes = mongo.db.recipes
        user = mongo.db.users.find_one({'username': session['username']})

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
            'username': session['username']
            }
        recipes.insert_one(enter_recipes)
        return redirect(url_for("my_recipes"))
    return redirect(url_for('access_denied'))


# Page with more details on the recipe
@app.route('/recipe_selected/<recipe_id>')
def recipe_selected(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template('recipe_selected.html', recipes=the_recipe,)


# Similar to add recipes. Logged in is required
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    if 'username' in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        categories = mongo.db.recipe_categories.find()
        return render_template(
            'edit_recipe.html',
            recipe=recipe,
            categories=categories
            )
    return redirect(url_for('access_denied'))


# updates the edited recipe in the database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    if 'username' in session:
        recipes = mongo.db.recipes
        recipes.update({'_id': ObjectId(recipe_id)}, {
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
            'username': session['username']
        })
        flash('recipe has been edited')
        return redirect(url_for('my_recipes'))
    return redirect(url_for('access_denied'))


# DELETE RECIPE
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    if 'username' in session:
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('my_recipes'))
    return redirect(url_for('access_denied'))


@app.route('/my_recipes')
def my_recipes():
    """
    searches recipes username field to see does it
    match the username in session.
    """
    if 'username' in session:
        per_page = 9
        recipes = mongo.db.recipes.find({'username': session['username']})
        page = request.args.get(get_page_parameter(), type=int, default=1)
        skips = per_page * (page - 1)
        cursor = recipes.skip(skips).limit(per_page)
        pagination = Pagination(
            page=page, total=recipes.count(),
            record_name='recipes', per_page=per_page,
            bs_version=4, css_framework='bootstrap',
            alignment='center'
            )
        return render_template(
            'my_recipes.html',
            recipes=recipes,
            pagination=pagination
            )
    return redirect(url_for('access_denied'))


# Clears the session cache to log the user out
@app.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
        flash("You've been successfully logged out")
        return redirect(url_for('get_recipes'))
    return redirect(url_for('access_denied'))


# If User doesn't have right to access the page
@app.route('/access_denied')
def access_denied():
    if 'username' in session:
        flash('You are logged in as ' + session['username'])
        return redirect(url_for('my_recipes'))
    return render_template('access_denied.html')


# 404 page
@app.errorhandler(404)
def response_404(exception):
    return render_template('error_handler.html')


# About Page 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False),
