from flask import Flask, render_template, jsonify, request
from flask_restful import reqparse, Resource, Api
from config import Configuration

import pandas

app = Flask(__name__)
api = Api(app)
cfg = Configuration(debug=True)

# Dummy data
CARDS = [
            {'id': 0,'name': '0', 'address': 'asdf', 'img': "", 'tags': [], 'costarHtml': "", 'costarCreated': 0, 'costarScore': 0, 'reference': [], 'score': "", 'price': 0},
            {'id': 1,'name': '1', 'address': 'qwer', 'img': "", 'tags': [], 'costarHtml': "", 'costarCreated': 0, 'costarScore': 0, 'reference': [], 'score': "", 'price': 0},
            {'id': 2,'name': '2', 'address': 'zxcv', 'img': "", 'tags': [], 'costarHtml': "", 'costarCreated': 0, 'costarScore': 0, 'reference': [], 'score': "", 'price': 0},
            {'id': 3,'name': '3', 'address': 'jkl;', 'img': "", 'tags': [], 'costarHtml': "", 'costarCreated': 0, 'costarScore': 0, 'reference': [], 'score': "", 'price': 0}
        ]

parser = reqparse.RequestParser()
parser.add_argument('id')

class testEndpoint(Resource):
    def get(self):
        return {'hello': 'world'}
class likeListing(Resource):
    def post(self):
        args = parser.parse_args()
        return {'id': args['id']}

api.add_resource(testEndpoint, '/')
api.add_resource(likeListing, '/like')


@app.route('/test')
def test_page():
    data = pandas.read_csv("database_outline.csv")
    data = data.to_dict('record')
    print(data)
    return render_template('swiping.html', cards=CARDS)




if __name__ == '__main__':
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)