import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manger'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
#MONGO_URI = os.environ.get("MONGO_URI")
#app.config["MONGO_URI"] = 'mongodb+srv://root:<password>@mycluster-pcvdt.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=(os.environ.get('PORT')),
        debug=True)