import os
from os import environ
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean
from plotly.offline import plot
import argparse
from flask import Markup
from flask import Flask
from flask import render_template


app = Flask(__name__)
populationSum = []
continents = []

class Generator:
    def __init__(self):
        server = environ.get("SERVER")
        user = environ.get("USER")
        password = environ.get("PASSWORD")
        dbname = environ.get("DBNAME")
        self.make(server,
                  user, dbname, password)

    def make(self, server, user, dbname, password):
        spark_session = SparkSession.builder.appName('winemap').getOrCreate()
        populationSum=[200,300,400]
        continents=['Europe','Africa','Asia']
      	//return render_template('chart.html', values=populationSum, labels=continents)

@app.route('/')
def index():
    Generator()
    return render_template('chart.html', values=populationSum, labels=continents)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
