from flask import Flask, render_template, jsonify, request
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from sqlalchemy import create_engine
from mysql.connector import MySQLConnection, Error
import csv
import pandas as pd
import pandas, os
import us

db_name = 'app.db'
cur_dir = os.path.join(os.path.dirname(__file__), db_name)
db_uri = 'sqlite:///{}'.format(cur_dir)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
cfg = Configuration(debug=True)
db = SQLAlchemy(app)
start = 0
stop = 25

coStarData = pandas.read_csv('data.csv')
statePics = pandas.read_csv('statePicRelation.csv')
def getCardsFromFile(start, stop):
    output = []
    for i in range(start, stop):
        temp = {}
        temp["id"] = coStarData['StoryID'][i]
        temp["name"] = coStarData["Title"][i]
        temp["costarCreated"] = coStarData["CreatedDate"][i]
        temp["costarHtml"] = (str(coStarData["Summary"][i]) + str(coStarData["Body"][i])).encode()
        if int(coStarData["Country_USA"][i]) == 1:
            address = "United States"
        elif int(coStarData["Country_CAN"][i]) == 1:
            address = "Canada"
        else:
            address = "Great Britain"
        temp["address"] = address
        img = "https://ahprd4cdn.csgpimgs.com/si2/JSZDDQlWHJFVRppsEo8-96vv-i7BIxrHlI6DXR1rDbJHIaY2fH8eJ1pCo-tus7zMoynmCfuUTvE9JAn705adpt6KOH3c7z_ppJqguUo2spM/1/image.jpg"
        # for j in range(len(list(coStarData["Title"][i]).split())):
        #     for k in range(len(us.states.STATES)):
        #         if coStarData["Title"][i].split()[j] == us.states.lookup(str(k)):
        #             img = statePics["pic"][list(statePics['state'][j]).index()]
        # Create later
        temp["img"] = img # placeholder image
        temp["tags"] = []
        temp["reference"] = []
        temp["score"] = []
        temp["price"] = 0.0
        temp["costarScore"] = []
        output.append(temp)
    return output

# Dummy data
CARDS = getCardsFromFile(start, stop)

parser = reqparse.RequestParser()
parser.add_argument('id')

class testEndpoint(Resource):
    def get(self):
        return {'hello': 'world'}
class likeListing(Resource):
    def post(self):
        args = parser.parse_args()
        # print(getCardsFromFile(start, stop)[0]['id'])
        return {'id': args['id']}

api.add_resource(testEndpoint, '/')
api.add_resource(likeListing, '/like')


@app.route('/test')
def test_page():
    return render_template('swiping.html', cards=CARDS)

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
    db.create_all()
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)