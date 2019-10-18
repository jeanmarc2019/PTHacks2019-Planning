from flask import Flask, render_template
from flask_restful import Resource, Api
from config import Configuration

app = Flask(__name__)
api = Api(app)
cfg = Configuration(debug=True)

class testEndpoint(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(testEndpoint, '/')
@app.route('/')
@app.route('/test')
# @app.route('/hello/<user>')
def test_page():
    return render_template('swiping.html')
if __name__ == '__main__':
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)