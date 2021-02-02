# import dependencies
import pandas as pd
import pymongo
from mongodb_upload import df_rows_todict, df_columns_todict, upload_db, update_db

def setup_game_db():
    
    # define csv to import
    csv = 'game_database_final.csv'
    
    # read csv and preview
    df = pd.read_csv(csv)
    
    # rename columns
    columns = ['game', 'month', 'hours_watched', 'average_viewers(k)', 'average_concurrent_streams(k)', 'peak_concurrent_streams(k)', 'peak_viewers(k)']
    df.columns = columns
    
    # format columns
#     df['month'] = pd.to_datetime(df['month'], format='%d/%m/%y')
    df['hours_watched'] = df['hours_watched'].map(lambda x: float(x.strip('M')) if 'M' in x else float(x.strip('K'))/1000000)
    df['average_viewers(k)'] = df['average_viewers(k)'].map(lambda x: float(x.strip('K')))
    df['average_concurrent_streams(k)'] = df['average_concurrent_streams(k)'].map(lambda x: float(x.strip('K')) if 'K' in x else float(x)/1000)
    df['peak_concurrent_streams(k)'] = df['peak_concurrent_streams(k)'].map(lambda x: float(x.strip('K')) if 'K' in x else float(x)/1000)
    df['peak_viewers(k)'] = df['peak_viewers(k)'].map(lambda x: float(x.strip('K')) if 'K' in x else float(x.strip('M'))*1000)

    # split data for each game into separate dataframes
    amongus_df = df.loc[df['game'] == 'Among Us']
    cod_df = df.loc[df['game'] == 'Call of Duty ']
    csgo_df = df.loc[df['game'] == 'Counter Strike Global Offensive']
    fortnite_df = df.loc[df['game'] == 'Fortnite']
    lol_df = df.loc[df['game'] == 'League of Legends ']
    
    # reset index and set month as index
    df_list = [amongus_df, cod_df, csgo_df, fortnite_df, lol_df]
    for x in df_list:
        x.reset_index(drop=True, inplace=True)
        x.set_index('month', inplace=True)
        
    return df_list

df_list = setup_game_db()

db_names = ['amongus_db', 'cod_db', 'csgo_db', 'fortnite_db', 'lol_db']
for index, value in enumerate(df_list):
    collection = db_names[index]
    df = df_list[index]
    dictionary = df_rows_todict(df)
    upload_db(collection, dictionary)