import requests
from requests import get
import urllib.request
import time
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from flask import jsonify

class Driver():
    @staticmethod
    def arne_is_gay():
        text = "Arne is gay and bachelor"
        return jsonify({'Arne the Project Manager who does nothing': text})

    @staticmethod
    def crawler(url):
        response = requests.get(url, timeout=5)

        soup = BeautifulSoup(response.content, "html.parser")

        all_links = soup.find_all("p")

        str_cells = str(all_links)
        cleantext = BeautifulSoup(str_cells, "lxml").get_text()

        print(cleantext)
        
        return jsonify(cleantext)

    @staticmethod
    def simple_get(url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                if Driver.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            Driver.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    @staticmethod
    def is_good_response(resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)


    @staticmethod
    def log_error(e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)