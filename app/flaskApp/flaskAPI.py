from flask import Flask, render_template, jsonify, request
from flask_restful import reqparse, Resource, Api
from config import Configuration

import pandas

app = Flask(__name__)
api = Api(app)
cfg = Configuration(debug=True)

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
    return render_template('swiping.html', data=data)

@app.route("/analysis", methods = ['POST', 'GET'])
def sentiment_analysis():

    if request.method == 'GET':
        return(render_template('search.html'))
    elif request.method == 'POST':
        city = request.form['city']
        state = request.form['state']
        year = request.form['year']
        keyword = request.form['keyword']



    return 0


if __name__ == '__main__':
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)