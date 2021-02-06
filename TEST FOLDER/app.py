# Import dependencies
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/project2")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # streamer_data = mongo.db.streamer_sorted_data.find_one({}, {'_id': False})
    streamer_data = mongo.db.streamer_sorted_data .find_one({}, {'_id': False})

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return render_template("index.html", streamer_data=streamer_data)

@app.route('/test')
def stations():
    streamer_data = mongo.db.streamer_sorted_data.find_one({}, {'_id': False})
    return streamer_data

@app.route('/games')
def games_page():
    return render_template("games.html")

@app.route('/games/<game>')
def game_profile(game):
    return 'This profile page is for ' + game

@app.route('/streamers')
def amongus():
    streamer = mongo.db.target_streamer.find_one({}, {'_id': False})
    return streamer

@app.route('/streamer/<channel>')
def streamer(channel):
    return 'welcome to profile page %s' %channel

if __name__ == "__main__":
    app.run(debug=True)