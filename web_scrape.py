# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from bs4 import re
import time
import requests
import pandas as pd

# Define function to start browser session for scraping
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# create function to scrape top streamers data
def scrape_top_steamers():
    # start browser
    browser = init_browser()
    # navigate to website
    browser.visit('https://twitchtracker.com/channels/viewership')
    # prepare soup for scraping
    html = browser.html
    soup = bs(html, 'html.parser')
    # find table body tag in html
    table_body = soup.find('tbody')
    # find all rows in table body
    streamers = table_body.findAll('tr')
    # create empty list to populate with each streamer's data
    streamers_list = []
    # for each streamer find the td tags and create an empty list to fill with data from each cell
    for streamer in streamers:
        table_cells = streamer.findAll('td')
        streamer_info = []
        for cell in table_cells:
            info = cell.get_text()
            streamer_info.append(info)
        streamers_list.append(streamer_info)
    # define list of column names for dataframe
    column_headers = ['avg_viewership_rank','picture','channel_name','avg_viewers','time_streamed','all_time_peak_viewers',
                     'hours_watched','overall_rank','followers_gained','total_followers','total_views']
    # create dataframe using streamers data and column names
    dataframe = pd.DataFrame(streamers_list, columns=column_headers)
    # set channel name as index
    dataframe.set_index('channel_name', inplace=True)
    # drop temporary column that was created for channel thumbnail
    dataframe.drop('picture', axis=1, inplace=True)
    # drop NAN row
    dataframe.dropna(inplace=True)
    # format each column to contain only numeric values
    dataframe['avg_viewership_rank'] = dataframe['avg_viewership_rank'].map(lambda x:int(x.strip('#')))
    dataframe['avg_viewers'] = dataframe['avg_viewers'].map(lambda x:int(x.replace(',','')))
    dataframe['time_streamed(hrs)'] = dataframe['time_streamed'].map(lambda x:float(x.strip('hours')) if 'hours' in x else float(x.strip('min'))/60)
    dataframe['all_time_peak_viewers'] = dataframe['all_time_peak_viewers'].map(lambda x:int(x.replace(',','')))
    dataframe['hours_watched'] = dataframe['hours_watched'].map(lambda x:int(float(x.strip('M'))*1000000) if 'M' in x else int(float(x.strip('K'))*1000))
    dataframe['overall_rank'] = dataframe['overall_rank'].map(lambda x:int(x))
    dataframe['followers_gained'] = dataframe['followers_gained'].map(lambda x:int(float(x.strip('\n+M'))*1000000) if 'M' in x else int(float(x.strip('\n+K'))*1000))
    dataframe['total_followers'] = dataframe['total_followers'].map(lambda x:int(float(x.strip('M'))*1000000) if 'M' in x else int(float(x.strip('K'))*1000))
    dataframe['total_views'] = dataframe['total_views'].map(lambda x:int(float(x.strip('M'))*1000000) if 'M' in x else int(float(x.strip('K'))*1000))
    
    return dataframe

def scrape_game_data(url):
    # start browser
    browser = init_browser()
    # navigate to website
    browser.visit(url)
    # prepare soup for scraping
    html = browser.html
    soup = bs(html, 'html.parser')
    # find html text that contains the title of the table we want to scrape from 
    target_title = soup.find_all(text=re.compile('Top Live')) 
    # find the header that has our target title and extract the text
    target_h4 = soup.find('h4', text=target_title)
    table_title = target_h4.get_text()
    # find tables that are in the same parent tag
    tables = target_h4.parent.findAll('table')

    # extract data from table into lists
    streamers = []
    viewers = []
    for column in tables:
        streamer_list = column.find_all('a')
        for streamer in streamer_list:
            streamer_name = streamer.get_text()
            streamers.append(streamer_name)
        viewers_list = column.find_all('span')
        for streamer in viewers_list:
            viewership = streamer.get_text()
            viewers.append(viewership)
    
    # close browser
    browser.quit()
    
    # create dictionary for use in dataframe using lists created 
    data_dict = {'Channel':streamers, 'Viewers':viewers}
    # create dataframe using dictionary created     
    mytable = pd.DataFrame(data_dict)
    # set the channel as the index
    mytable.set_index('Channel', inplace=True)
    return mytable

def scrape_streamer_data(url):
    # start browser
    browser = init_browser()
    # navigate to website
    browser.visit(url)
    #click on month tab in performace section
    browser.find_by_text('Month').click()
    # prepare soup for scraping
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # create empty dictionary to store data we scrape
    data_dict = {}
    
    # scrape for channel_name
    channel_name = soup.find('div', id='mini-profile').find('h4').get_text()
    data_dict['channel_name'] = channel_name
    
    # scrape for streamer's avg_viewers
    target_text = soup.find_all(text=re.compile('Avg viewers'))
    target_div = soup.find('div', text=target_text)
    avg_viewers = float(target_div.parent.find_all('span')[1].get_text().replace(',',''))
    data_dict['avg_viewers'] = avg_viewers
    
    # scrape for streamer's time_streamed
    target_text = soup.find_all(text=re.compile('Hours streamed'))
    target_div = soup.find('div', text=target_text)
    time_streamed = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['time_streamed(hrs)'] = time_streamed
    
    # scrape for streamer's all_time_peak_viewers
    target_text = soup.find_all(text=re.compile('Highest recorded number of concur. viewers'))
    target_div = soup.find('div', text=target_text)
    all_time_peak_viewers = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['all_time_peak_viewers'] = all_time_peak_viewers

    # scrape for streamer's hours_watched
    target_text = soup.find_all(text=re.compile('Hours watched'))
    target_div = soup.find('div', text=target_text)
    hours_watched = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['hours_watched'] = hours_watched

    # scrape for streamer's overall_rank
    target_text = soup.find_all(text=re.compile('RANK'))
    target_div = soup.find('span', text=target_text)
    overall_rank = float(target_div.parent.find_all('span')[1].get_text().replace(',',''))
    data_dict['overall_rank'] = overall_rank

    # scrape for streamer's followers_gained
    target_text = soup.find_all(text=re.compile('Followers gained'))
    target_div = soup.find('div', text=target_text)
    followers_gained = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['followers_gained'] = followers_gained
    
    # scrape for streamer's total_followers
    target_text = soup.find_all(text=re.compile('Total followers'))
    target_div = soup.find('div', text=target_text)
    total_followers = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['total_followers'] = total_followers
    
    # scrape for streamer's total_views
    target_text = soup.find_all(text=re.compile('Total views'))
    target_div = soup.find('div', text=target_text)
    total_views = float(target_div.parent.find_all('div')[2].get_text().replace(',',''))
    data_dict['total_views'] = total_views

    # close browser
    browser.quit()
    
    # create dataframe using dictionary created     
    mytable = pd.DataFrame([data_dict])
    # set the channel as the index
    mytable.set_index('channel_name', inplace=True)
    return mytable