from flaskAPI import app, db
import mysql.connector
import pandas, os
from sqlalchemy import create_engine

docker = True
if not docker:
    db_name = 'app'
    cur_dir = os.path.join(os.path.dirname(__file__), db_name)
    db_uri = 'mysql:///{}'.format(cur_dir)
else:
    db_uri = 'mysql+mysqlconnector://root:tester@mysql/app'
e = create_engine(db_uri)

dataset = pandas.read_csv('data.csv')

dataset.to_sql(name='dataset', con=e)

#for index, row in dataset.iterrows():
#    print(row['Body'])