# import necessary libraries
from flask import (
    Flask, 
    render_template, 
    redirect, 
    jsonify,
    request
    )
from flask_pymongo import PyMongo
from Card_Deck_Hand import Card, Deck, Hand
import json
import jinja2

# create instance of Flask app
app = Flask(__name__)

# add configuration as Heroku requirement
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug

# Create MLAB db connection for mongodb that works with heroku app
# mongo_uri = 'mongodb://heroku_x58zdhbn:fb7o0k7stbsk0ivbirarr2i2d3@ds139775.mlab.com:39775/heroku_x58zdhbn'
# app.config['MONGO_URI'] = mongo_uri
# mongo = PyMongo(app,uri=mongo_uri)ASD

@app.route('/')
def index():
    return render_template('home.html')




 






if __name__ == '__main__':
  app.run(debug=True)