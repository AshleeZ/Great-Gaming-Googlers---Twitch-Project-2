# Import dependencies
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from web_scrape import scrape_top_steamers, scrape_game_data, scrape_streamer_data
from mongodb_upload import df_rows_todict, df_columns_todict, upload_db, update_db

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

@app.route('/about')
def about():
    return 'This is our ABOUT page.'

@app.route('/topstreamers')
def top_streamers():
    return 'This is our TOP STREAMERS page.'

@app.route('/games')
def games_page():
    return render_template("games.html", game = 'Choose a Game to View the Top 20 Twitch Channels Streaming It')

@app.route('/ourteam')
def our_team():
    return 'This is our TEAM page.'

@app.route('/games/<game>')
def game_profile(game):
    games_dict = {'leagueoflegends':'21779', 'dota2':'29595', 'smite':'32507', 'fortnite':'33214', 'callofduty':'512710', 'csgo':'32399', 'chess':'743', 'amongus':'510218', 'hearthstone':'138585'}
    game_string = game.lower().replace(' ','')
    game_code = games_dict[game_string]
    url = 'https://twitchtracker.com/games/' + game_code
    df = scrape_game_data(url)
    dictionary = df_rows_todict(df)
    collection = 'target_game'
    upload = update_db(collection, dictionary)
    return render_template('games.html', game = game)

@app.route('/targetgamedata')
def game_data():
    game_data = mongo.db.target_game.find_one({}, {'_id': False})
    return game_data

@app.route('/streamer/<channel>')
def streamer(channel):
    channel_name = channel.lower()
    url = 'https://twitchtracker.com/' + channel_name
    df = scrape_streamer_data(url)
    dictionary = df_rows_todict(df)
    collection = 'target_streamer'
    upload = update_db(collection, dictionary)
    return render_template('streamer.html')

@app.route('/targetstreamerdata')
def streamer_data():
    streamer_data = mongo.db.target_streamer.find_one({}, {'_id': False})
    return streamer_data

if __name__ == "__main__":
    app.run(debug=True)