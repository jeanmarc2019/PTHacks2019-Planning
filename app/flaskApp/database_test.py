from flaskAPI import app, db
import pandas
dataset = pandas.read_csv('data.csv')

for index, row in dataset.iterrows():
    print(row['Body'])