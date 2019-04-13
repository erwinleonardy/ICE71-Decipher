from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"*/arne/*": {"origins": "*"}})

from crawler import routes