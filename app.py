# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from web_scrape import scrape_top_steamers, scrape_game_data
from mongodb_upload import df_rows_todict, df_columns_todict, upload_db, update_db

# # scrape top streamers on launch
# top_streamers = scrape_top_steamers()

# scrape game data
url = "https://twitchtracker.com/games/21779"
game_data = scrape_game_data(url)

# convert game dataframe to dictionaries
rows_dict = df_rows_todict(game_data)
columns_dict = df_columns_todict(game_data)

# # convert dataframe to dictionaries
# rows_dict = df_rows_todict(top_streamers)
# columns_dict = df_columns_todict(top_streamers)

# # upload streamer data to database
# collection = 'streamer_sorted_data'
# upload_db(collection, rows_dict)
# collection = 'metrics_sorted_data'
# upload_db(collection, columns_dict)

# upload game data to database
# collection = 'game_data'
# upload_db(collection, rows_dict)

# update game data database instead
collection = 'game_data'
update_db(collection, rows_dict)


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/project2")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # streamer_data = mongo.db.streamer_sorted_data.find_one({}, {'_id': False})
    game_data = mongo.db.game_data.find_one({}, {'_id': False})

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return render_template("index.html", game_data=game_data)

if __name__ == "__main__":
    app.run(debug=True)