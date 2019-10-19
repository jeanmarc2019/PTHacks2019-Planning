from flaskAPI import app, db
import pandas, os
from sqlalchemy import create_engine

db_name = 'app.db'
cur_dir = os.path.join(os.path.dirname(__file__), db_name)
db_uri = 'sqlite:///{}'.format(cur_dir)
e = create_engine(db_uri)

dataset = pandas.read_csv('data.csv')

dataset.to_sql(name='dataset', con=e)

#for index, row in dataset.iterrows():
#    print(row['Body'])