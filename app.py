import os
from os import environ
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean
from plotly.offline import plot
import argparse
from flask import Flask, render_template


app = Flask(__name__)


class WineMapGenerator:

    def __init__(self):
        server = environ.get("SERVER")
        user = environ.get("USER")
        password = environ.get("PASSWORD")
        dbname = environ.get("DBNAME")
        self.make(server,
                  user, dbname, password)

    def make(self, server, user, dbname, password):
        #spark_session = SparkSession.builder.appName('winemap').getOrCreate()
      	


def make_template():
    # make the templates dir
    new_path = '/opt/app-root/src/templates'
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        # move the file to the templates dir
        shutil.move('/opt/app-root/src/map.html', new_path)
    return render_template("map.html", title='Maps')

@app.route('/')
def index():
    spark_session = SparkSession.builder.appName('winemap').getOrCreate()
    return 'halllooo'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
