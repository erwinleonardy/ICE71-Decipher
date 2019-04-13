from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/crawl/*": {"origins": "*"}}, supports_credentials=True)

from crawler import routes