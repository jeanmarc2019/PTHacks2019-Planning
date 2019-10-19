from flask import Flask, render_template
from flask_restful import Resource, Api
from config import Configuration

import pandas

app = Flask(__name__)
api = Api(app)
cfg = Configuration(debug=True)

class testEndpoint(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(testEndpoint, '/')
@app.route('/')
@app.route('/test')
def test_page():
    data = pandas.read_csv("database_outline.csv")
    data = data.to_dict('record')
    print(data)
    return render_template('swiping.html', data=data)


if __name__ == '__main__':
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)