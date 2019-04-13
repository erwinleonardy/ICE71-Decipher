from crawler import app
from crawler.driver import Driver

@app.route('/')
def index():
    print("Hello\n")
    return Driver.arne_is_great()