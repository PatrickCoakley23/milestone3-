import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'milestone3'
app.config["MONGO_URI"] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route('/')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)