from crawler import app
from crawler.driver import Driver

@app.route('/arne/is/gay/and/bachelor', methods=['GET'])
def get_tasks():
    return Driver.arne_is_gay()
