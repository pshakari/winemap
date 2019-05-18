import os
from os import environ
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean
from plotly.offline import plot
import argparse
from flask import Flask
import sys
import optparse
import time
from flask import Markup
from flask import Flask
from flask import render_template


app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():
    server = environ.get("SERVER")
    user = environ.get("USER")
    password = environ.get("PASSWORD")
    dbname = environ.get("DBNAME")
    
    spark_session = SparkSession.builder.appName('winemap').getOrCreate()   
    #df = spark_session.read.format("jdbc").options(url=url,dbtable="population",driver="org.postgresql.Driver").load()
    #table = df.select('continent', 'sum(population) population').groupBy('continent').orderBy('population', ascending=False)
    continents = []#table.select('continent').collect()
    populationSum = []#table.select('population').collect()		
		
    return render_template('chart.html', values=populationSum, labels=continents)

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python app.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
