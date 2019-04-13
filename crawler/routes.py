import requests
from requests import get
from bs4 import BeautifulSoup

from crawler import app
from crawler.driver import Driver

@app.route('/')
def index():
    url = 'https://en.wikipedia.org/wiki/Donald_Trump'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    all_links = soup.find_all("p")

    str_cells = str(all_links)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()

    print(cleantext)

    #print(response)

    return cleantext

@app.route('/arne/is/gay/and/bachelor', methods=['GET'])
def get_tasks():
    return Driver.arne_is_gay()
