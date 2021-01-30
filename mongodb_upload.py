# import dependencies
import pymongo
import pandas as pd

# function for converting dataframe to dictionary with rows as main keys 
def df_rows_todict(dataframe):
    df_dict = {}
    for index, row in dataframe.iterrows():
        column_values = row.to_dict()
        df_dict[index] = column_values
    return df_dict

# function for converting dataframe to dictionary with columns as main keys
def df_columns_todict(dataframe):
    return dataframe.to_dict()

# define function for uploading data to mongodb
def upload_db(collection, dictionary):
    db_name = 'project2'
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[db_name]
    mycol = mydb[collection]
    # error handling in case collection already exists in database
    try:
        upload = mycol.insert_one(dictionary)
    except:
        print('This collection already exists. Change collection name or delete collection in mongodb before trying again.')

# define function for update database with new data
def update_db(collection, dictionary):
    db_name = 'project2'
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient[db_name]
    mycol = mydb[collection]
    # error handling in case collection already exists in database
    try:
        mycol.drop()
        update = mycol.insert_one(dictionary)
    except:
        print('This collection already exists. Change collection name or delete collection in mongodb before trying again.')   