from flask import jsonify

class Driver():
    @staticmethod
    def arne_is_great():
        text = "Arne is superb"
        return text
        # return jsonify(text)