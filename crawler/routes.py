import requests
from requests import get
from bs4 import BeautifulSoup
from flask_cors import CORS

from crawler import app
from crawler.driver import Driver

@app.route('/crawl')
def index():
    print("IN\n\n\n\n\n\n")
    url = 'https://en.wikipedia.org/wiki/Donald_Trump'
    return Driver.crawler(url)

@app.route('/api/arne/is/gay/and/bachelor', methods=['GET', 'POST'])
def get_tasks():
    if requests.method == 'POST':
        print (requests.form['form'])
        return Driver.arne_is_gay()

# @app.route('/url', methods=['POST'])
# def get_route():
#     print (requests.form)
#     return Driver.arne_is_gay()

# @app.route('/exclude', methods=['POST'])
# def get_exclude():
#     print (requests.form)
#     return Driver.arne_is_gay()
