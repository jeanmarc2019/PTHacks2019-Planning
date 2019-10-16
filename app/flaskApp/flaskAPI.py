from flask import Flask, render_template
from flask_restful import Resource, Api
from config import Configuration

app = Flask(__name__)
api = Api(app)
cfg = Configuration(debug=True)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
@app.route('/')
@app.route('/test')
# @app.route('/hello/<user>')
def hello_world():
    return render_template('base.html', user='tester')
if __name__ == '__main__':
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)