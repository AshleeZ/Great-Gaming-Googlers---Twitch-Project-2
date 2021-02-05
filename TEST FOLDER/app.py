# Import dependencies
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import pandas as pd

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
    # Find one record of data from the mongo database
    # streamer_data = mongo.db.streamer_sorted_data.find_one({}, {'_id': False})
    streamer_data = mongo.db.streamer_sorted_data .find_one({}, {'_id': False})


    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return streamer_data




@app.route('/test3')
def hours_watched(): 
    # Find one record of data from the mongo database
    # streamer_data = mongo.db.streamer_sorted_data.find_one({}, {'_id': False})
    streamer_data = mongo.db.streamer_sorted_data .find_one({}, {'_id': False})


    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return streamer_data

if __name__ == "__main__":
    app.run(debug=True)

















# @app.route('/game')
# def games():
#     # Find one record of data from the mongo database
#     cod_data = mongo.db.cod_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
#     table = pd.DataFrame(cod_data)
#     new_table = table.transpose()
#     new_table.index = pd.to_datetime(new_table.index)
#     new_table.sort_index(inplace=True)
#     new_table.index = pd.to_datetime(new_table.index)
#     new_table.reset_index(level=0, inplace=True)
#     new_table['index']=pd.to_datetime(new_table['index'])
#     df = new_table[['index', 'average_viewers(k)']]
#     df.sort_values(by = ['index'])
#     new_df = df.copy()
#     new_df['index'] = new_df['index'].astype(str)
#     y = new_df.set_index('index').T.to_dict('list')
    

#     # Return template and data
#     # return render_template("index.html", streamer_data=streamer_data)
#     return y
