from flask import jsonify

class Driver():
    @staticmethod
    def arne_is_gay():
        text = "Arne is gay and bachelor"
        return jsonify({'Arne the Project Manager who does nothing': text})