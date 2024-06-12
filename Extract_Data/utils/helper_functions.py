from ftfy import fix_text
import requests
import hashlib
import time
import os
from dotenv import load_dotenv
import pandas as pd
from bs4 import BeautifulSoup
load_dotenv(dotenv_path='.env')
API_KEY = os.getenv('MARVEL_API_KEY')
PUBLIC_KEY = os.getenv('MARVEL_PUBLIC_KEY')


#sends back in 100 characters from the marvel api
def get_100_characters(offset,limit=100):
    
    
    ts = str(int(time.time())) #for hashing
    hash_str = hashlib.md5((ts + API_KEY + PUBLIC_KEY).encode('utf-8')).hexdigest() #hasing
    
    #returns the characters in json format
    return requests.get(
    f'http://gateway.marvel.com/v1/public/characters',
    params={
        "apikey": PUBLIC_KEY,
        'ts':ts,
        "hash": hash_str,
        "limit":limit,
        "offset":offset,
        
    }
    ).json()['data']['results']
    ##########
    


def clean_html(text):
    if pd.isna(text):
        return text
    
    if '<' in text and '>' in text:
        return BeautifulSoup(text, 'lxml').get_text()
    return text


def clean_text(text):
    if pd.isna(text):
        return text
    return fix_text(text)


def clean_data(text):
    text = clean_html(text)
    text= clean_text(text)
    return text.replace('ÔøΩ', "'")