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