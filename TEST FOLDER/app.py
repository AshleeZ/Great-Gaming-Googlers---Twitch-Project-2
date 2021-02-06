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



@app.route('/cod')
def cod_database():
    # Find one record of data from the mongo database
    cod_data = mongo.db.cod_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
    table = pd.DataFrame(cod_data)
    new_table = table.transpose()
    new_table.index = pd.to_datetime(new_table.index)
    new_table.sort_index(inplace=True)
    new_table.index = pd.to_datetime(new_table.index)
    new_table.reset_index(level=0, inplace=True)
    new_table['index']=pd.to_datetime(new_table['index'])
    df = new_table[['index', 'average_viewers(k)']]
    df.sort_values(by = ['index'])
    new_df = df.copy()
    new_df['index'] = new_df['index'].astype(str)
    cod = new_df.set_index('index').T.to_dict('list')

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return cod




@app.route('/among_us')
def amongus_database():
    # Find one record of data from the mongo database
    amongus_data = mongo.db.amongus_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
    table = pd.DataFrame(amongus_data)
    new_table = table.transpose()
    new_table.index = pd.to_datetime(new_table.index)
    new_table.sort_index(inplace=True)
    new_table.index = pd.to_datetime(new_table.index)
    new_table.reset_index(level=0, inplace=True)
    new_table['index']=pd.to_datetime(new_table['index'])
    df = new_table[['index', 'average_viewers(k)']]
    df.sort_values(by = ['index'])
    new_df = df.copy()
    new_df['index'] = new_df['index'].astype(str)
    amongus = new_df.set_index('index').T.to_dict('list')
    

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return amongus


@app.route('/csgo')
def csgo_database():
    # Find one record of data from the mongo database
    csgo_data = mongo.db.csgo_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
    table = pd.DataFrame(csgo_data)
    new_table = table.transpose()
    new_table.index = pd.to_datetime(new_table.index)
    new_table.sort_index(inplace=True)
    new_table.index = pd.to_datetime(new_table.index)
    new_table.reset_index(level=0, inplace=True)
    new_table['index']=pd.to_datetime(new_table['index'])
    df = new_table[['index', 'average_viewers(k)']]
    df.sort_values(by = ['index'])
    new_df = df.copy()
    new_df['index'] = new_df['index'].astype(str)
    cs_go = new_df.set_index('index').T.to_dict('list')
    

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return cs_go

@app.route('/fortnite')
def fortnite_database():
    # Find one record of data from the mongo database
    fortnite_data = mongo.db.fortnite_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
    table = pd.DataFrame(fortnite_data)
    new_table = table.transpose()
    new_table.index = pd.to_datetime(new_table.index)
    new_table.sort_index(inplace=True)
    new_table.index = pd.to_datetime(new_table.index)
    new_table.reset_index(level=0, inplace=True)
    new_table['index']=pd.to_datetime(new_table['index'])
    df = new_table[['index', 'average_viewers(k)']]
    df.sort_values(by = ['index'])
    new_df = df.copy()
    new_df['index'] = new_df['index'].astype(str)
    fort_nite = new_df.set_index('index').T.to_dict('list')
    

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return fort_nite

@app.route('/lol')
def lol_database():
    # Find one record of data from the mongo database
    lol_data = mongo.db.lol_db.find_one({}, {'_id': False}, sort=[('hours_watched', 1)])
    table = pd.DataFrame(lol_data)
    new_table = table.transpose()
    new_table.index = pd.to_datetime(new_table.index)
    new_table.sort_index(inplace=True)
    new_table.index = pd.to_datetime(new_table.index)
    new_table.reset_index(level=0, inplace=True)
    new_table['index']=pd.to_datetime(new_table['index'])
    df = new_table[['index', 'average_viewers(k)']]
    df.sort_values(by = ['index'])
    new_df = df.copy()
    new_df['index'] = new_df['index'].astype(str)
    l_o_l= new_df.set_index('index').T.to_dict('list')
    

    # Return template and data
    # return render_template("index.html", streamer_data=streamer_data)
    return l_o_l


if __name__ == "__main__":
    app.run(debug=True)















# RIP DANNY #

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
