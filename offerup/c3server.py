from flask import Flask, jsonify
from .c3 import C3

app = Flask(__name__)


@app.route('/convos')
def get_convos():
    c3 = C3('conversations', 'offerup')
    convos = list(c3.container.read_all_items())
    return jsonify(convos)


if __name__ == '__main__':
    app.run()
