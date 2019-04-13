import requests
from requests import get
from bs4 import BeautifulSoup

from crawler import app
from crawler.driver import Driver

@app.route('/')
def index():
    url = 'https://en.wikipedia.org/wiki/Donald_Trump'
    return Driver.crawler(url)

@app.route('/arne/is/gay/and/bachelor', methods=['GET'])
def get_tasks():
    return Driver.arne_is_gay()
